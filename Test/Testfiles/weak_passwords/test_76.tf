variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_instance" "ycjnwibsiu" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_instance.ycjnwibsiu.ssh_key
}

module "secure_module" {
  source = "./modules/myturywpay"
  ssh_key = var.ssh_key
}
