variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_db_instance" "npaoxuoraf" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_db_instance.npaoxuoraf.private_key
}

module "secure_module" {
  source = "./modules/xifcknileh"
  private_key = var.private_key
}
