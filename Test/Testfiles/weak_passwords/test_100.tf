variable "password" {
  description = "The password"
  type = string
}

resource "aws_instance" "mkygguvzzb" {
  password = var.password
}

output "password" {
  value = aws_instance.mkygguvzzb.password
}

module "secure_module" {
  source = "./modules/dbvxmtvkpi"
  password = var.password
}
