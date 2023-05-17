variable "access_key" {
  description = "The access_key"
  type = string
}

resource "aws_db_instance" "vogdasijcj" {
  access_key = var.access_key
}

output "access_key" {
  value = aws_db_instance.vogdasijcj.access_key
}

module "secure_module" {
  source = "./modules/wfktraobwz"
  access_key = var.access_key
}
