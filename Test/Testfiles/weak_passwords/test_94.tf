variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_security_group" "viutaohkfa" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_security_group.viutaohkfa.ssh_key
}

module "secure_module" {
  source = "./modules/yfjqwgtowy"
  ssh_key = var.ssh_key
}
