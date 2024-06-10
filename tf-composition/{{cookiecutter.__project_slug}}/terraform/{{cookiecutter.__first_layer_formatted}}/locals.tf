locals {
  ############################################
  #                 GENERAL                  #
  ############################################

  full_name = "${var.client}-${var.app}-${var.environment}"

  # Example

  # Add others locals here
  filename = "${var.filename}-${var.environment}.txt"

  tags = merge(var.tags,
    {
      Name        = local.full_name
      client      = var.client,
      env_type    = var.env_type,
      app         = var.app,
      environment = var.environment
    }
  )
}
