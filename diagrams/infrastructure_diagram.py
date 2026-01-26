#!/usr/bin/env python3
from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS, ECR, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, CloudFront, Route53
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM, Cognito
from diagrams.aws.integration import SQS
from diagrams.aws.general import Users

# Create the diagram
with Diagram("AWS Architecture", show=True, direction="TB"):

    # Define users
    users = Users("End Users")

    # DNS and CDN
    with Cluster("DNS and Content Delivery"):
        dns = Route53("Route 53")
        cdn = CloudFront("CloudFront")

    # Frontend
    with Cluster("Frontend"):
        s3 = S3("Angular Frontend")

    # Authentication
    with Cluster("Authentication"):
        cognito = Cognito("User Authentication")

    # Backend Services
    with Cluster("Backend Services"):
        lb = ELB("Load Balancer")

        with Cluster("Container Services"):
            ecr = ECR("Container Registry")
            ecs = ECS("ECS Cluster")

        with Cluster("Database"):
            rds = RDS("RDS Database")

        with Cluster("Auxiliary Services"):
            lambda_fn = Lambda("Lambda Functions")
            queue = SQS("Message Queue")

    # Define the flow
    users >> dns >> cdn >> s3
    users >> cognito
    cdn >> lb >> ecs
    ecs >> rds
    ecs >> lambda_fn
    lambda_fn >> queue
    ecr >> ecs

    # IAM permissions across all services
    iam = IAM("IAM Roles & Policies")
    iam - [s3, ecs, rds, lambda_fn, queue]
