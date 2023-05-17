variable "ssh_key" {
  description = "The ssh_key"
  type = string
}

resource "aws_db_instance" "ygnipekrkk" {
  ssh_key = var.ssh_key
}

output "ssh_key" {
  value = aws_db_instance.ygnipekrkk.ssh_key
}

module "secure_module" {
  source = "./modules/qbiafhjoym"
  ssh_key = var.ssh_key
}
