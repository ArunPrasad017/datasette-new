provider "aws" {
    region = "us-east-1"
}

resource "aws_s3_bucket" "bucket1"{
    bucket = "arun-datasette-bucket"
    acl = "private"
    versioning{
        enabled = true
    }
    tags ={
        Name = "test-bucket"
        Environment = "test"
    }
}

terraform {
  backend "s3" {
    bucket  = "arun-useast1-dev-infra"
    key     = "state/s3/s3_test.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}
