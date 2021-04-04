resource "aws_s3_bucket" "bucket1"{
    bucket = "arun-tf-s3-bucket"
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
    bucket  = "aruntestbucketaws"
    key     = "state/s3/s3_test.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}
