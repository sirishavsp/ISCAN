variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_db_instance" "awmsontmfs" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_db_instance.awmsontmfs.pwd
}

module "secure_module" {
  source = "./modules/cbydkpestm"
  pwd = var.pwd
}
