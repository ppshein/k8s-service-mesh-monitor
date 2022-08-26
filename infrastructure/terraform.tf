terraform {
  required_version = ">= 0.13"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }

  backend "s3" {
    region         = "ap-southeast-1"
    role_arn       = "arn:aws:iam::xxxxxxxxxx:role/aws-admin"
    bucket         = "opsmo-devops-tfstate-ap"
    key            = "eks-poc-terraform.tfstate"
    dynamodb_table = "opsmo-devops-tfstate-ap-lock"
    encrypt        = true
  }
}
