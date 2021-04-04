resource "aws_elastic_beanstalk_application" "datasette_docker_app" {
  name        = "datasette-docker-app"
  description = "placeholder datasette-docker-app for deploying datasette image to elbs environment"
}

resource "aws_elastic_beanstalk_environment" "datasette_docker_env" {
  name                = "datasette-docker-env"
  application         = aws_elastic_beanstalk_application.datasette_docker_app.name
  solution_stack_name = "64bit Amazon Linux 2 v3.2.6 running Docker"
  tier                = "WebServer"
}