variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_instance" "qlptlyakau" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_instance.qlptlyakau.ssh_key
}

module "secure_module" {
  source = "./modules/ttmcywqsbp"
  ssh_key = var.ssh_key
}
