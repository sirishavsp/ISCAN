variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_instance" "bovlitvfnn" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_instance.bovlitvfnn.pwd
}

module "secure_module" {
  source = "./modules/cdxbeeugxy"
  pwd = var.pwd
}
