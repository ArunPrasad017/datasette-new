resource "aws_s3_bucket" "bucket1"{
    bucket = "test-s3-bucket"
    acl = "private"
    versioning{
        enabled = true
    }
    tags ={
        Name = "test-bucket"
        Environment = "test"
    }
}