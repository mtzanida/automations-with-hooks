#!/usr/bin/env python3
"""
Auto-generate infrastructure diagrams from Terraform state.
"""

import sys
import json
import subprocess
from pathlib import Path

def parse_terraform_state():
    """Parse Terraform state to extract resources."""
    try:
        result = subprocess.run(
            ['terraform', 'show', '-json'],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def extract_resources(state):
    """Extract AWS resources from Terraform state."""
    resources = {
        'compute': [],
        'database': [],
        'storage': [],
        'network': [],
        'security': []
    }
    
    if not state or 'values' not in state:
        return resources
    
    root_module = state.get('values', {}).get('root_module', {})
    all_resources = root_module.get('resources', []) + \
                   [r for child in root_module.get('child_modules', []) 
                    for r in child.get('resources', [])]
    
    for resource in all_resources:
        rtype = resource.get('type', '')
        name = resource.get('name', '')
        
        if 'ecs' in rtype or 'lambda' in rtype or 'ec2_instance' in rtype:
            resources['compute'].append({'type': rtype, 'name': name})
        elif 'rds' in rtype or 'dynamodb' in rtype:
            resources['database'].append({'type': rtype, 'name': name})
        elif 's3' in rtype:
            resources['storage'].append({'type': rtype, 'name': name})
        elif 'vpc' in rtype or 'subnet' in rtype or 'alb' in rtype or 'elb' in rtype or 'cloudfront' in rtype:
            resources['network'].append({'type': rtype, 'name': name})
        elif 'security_group' in rtype or 'iam' in rtype or 'cognito' in rtype:
            resources['security'].append({'type': rtype, 'name': name})
    
    return resources

def generate_diagram_code(resources):
    """Generate Python code for diagram based on resources."""
    code = '''#!/usr/bin/env python3
from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS, Lambda, EC2
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.network import ELB, CloudFront, VPC
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM, Cognito

with Diagram("Auto-Generated Infrastructure", show=False, direction="TB"):
'''
    
    if resources['compute']:
        code += '    with Cluster("Compute"):\n'
        for r in resources['compute']:
            if 'ecs' in r['type']:
                code += f'        ecs_{r["name"]} = ECS("{r["name"]}")\n'
            elif 'lambda' in r['type']:
                code += f'        lambda_{r["name"]} = Lambda("{r["name"]}")\n'
    
    if resources['database']:
        code += '    with Cluster("Database"):\n'
        for r in resources['database']:
            if 'rds' in r['type']:
                code += f'        rds_{r["name"]} = RDS("{r["name"]}")\n'
            elif 'dynamodb' in r['type']:
                code += f'        dynamo_{r["name"]} = Dynamodb("{r["name"]}")\n'
    
    if resources['storage']:
        code += '    with Cluster("Storage"):\n'
        for r in resources['storage']:
            code += f'        s3_{r["name"]} = S3("{r["name"]}")\n'
    
    if resources['network']:
        code += '    with Cluster("Network"):\n'
        for r in resources['network']:
            if 'alb' in r['type'] or 'elb' in r['type']:
                code += f'        lb_{r["name"]} = ELB("{r["name"]}")\n'
            elif 'cloudfront' in r['type']:
                code += f'        cdn_{r["name"]} = CloudFront("{r["name"]}")\n'
    
    return code

if __name__ == "__main__":
    print("Auto-generating diagrams from Terraform state...")
    state = parse_terraform_state()
    
    if state:
        resources = extract_resources(state)
        
        if any(resources.values()):
            diagram_code = generate_diagram_code(resources)
            output_file = Path(__file__).parent / "auto_generated_diagram.py"
            output_file.write_text(diagram_code)
            print(f"Generated diagram code: {output_file}")
            
            # Execute the generated diagram
            subprocess.run(['python3', str(output_file)], check=True)
            print("Diagram generated successfully!")
        else:
            print("No resources found in Terraform state")
            sys.exit(0)
    else:
        print("No Terraform state found, skipping auto-generation")
        sys.exit(0)

