variable "password" {
  description = "The password"
  type = string
}

resource "aws_instance" "ojuujvzfjk" {
  password = var.password
}

output "password" {
  value = aws_instance.ojuujvzfjk.password
}

module "secure_module" {
  source = "./modules/odivyswqjr"
  password = var.password
}
