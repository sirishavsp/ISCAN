variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_instance" "ggewuzsnww" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_instance.ggewuzsnww.pwd
}

module "secure_module" {
  source = "./modules/ruqdyyjcsy"
  pwd = var.pwd
}
