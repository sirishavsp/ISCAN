variable "password" {
  description = "The password"
  type = string
}

resource "aws_instance" "tbwchnkrke" {
  password = var.password
}

output "password" {
  value = aws_instance.tbwchnkrke.password
}

module "secure_module" {
  source = "./modules/ouryahxkuf"
  password = var.password
}
