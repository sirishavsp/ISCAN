variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_instance" "xvskljejrg" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_instance.xvskljejrg.pwd
}

module "secure_module" {
  source = "./modules/lrntowwvom"
  pwd = var.pwd
}
