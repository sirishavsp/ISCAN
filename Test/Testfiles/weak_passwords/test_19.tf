variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_security_group" "xtfjdsdlja" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_security_group.xtfjdsdlja.pwd
}

module "secure_module" {
  source = "./modules/dpifqkdbhj"
  pwd = var.pwd
}
