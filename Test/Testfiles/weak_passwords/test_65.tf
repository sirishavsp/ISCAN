variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_db_instance" "rhxbngkhnn" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_db_instance.rhxbngkhnn.pwd
}

module "secure_module" {
  source = "./modules/ovdagkjbvd"
  pwd = var.pwd
}
