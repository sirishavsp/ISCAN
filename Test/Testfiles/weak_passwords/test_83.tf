variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_db_instance" "varynscjuv" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_db_instance.varynscjuv.ssh_key
}

module "secure_module" {
  source = "./modules/htlmnibzje"
  ssh_key = var.ssh_key
}
