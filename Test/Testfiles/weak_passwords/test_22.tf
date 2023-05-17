variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_instance" "ajryqbrnjt" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_instance.ajryqbrnjt.ssh_key
}

module "secure_module" {
  source = "./modules/iztmxtgbqp"
  ssh_key = var.ssh_key
}
