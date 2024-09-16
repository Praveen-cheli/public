providers "aws"{
region = "us-east-1"
}
resource "aws_instance" "myINs"{
 ami = "ami-12423dfer45qeer"
 instance_type = "t2.micro"
}
