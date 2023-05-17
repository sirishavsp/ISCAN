variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_db_instance" "qcanyrvvqe" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_db_instance.qcanyrvvqe.access_key
}

module "secure_module" {
  source = "./modules/hhrhhhmysg"
  access_key = var.access_key
}
