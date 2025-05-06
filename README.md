# 🔐 Runner Terraform with 1Password CLI

A Docker image based on Spacelift's runner-terraform image with the 1Password CLI installed.

## 📖 Overview

This repository builds a Docker image based on `public.ecr.aws/spacelift/runner-terraform`, adding the 1Password CLI (`op`). The image is automatically updated when new versions of the 1Password CLI are released.

## ⏰ Automated Updates

This repository uses GitHub Actions to automatically check for new 1Password CLI versions and build new images when updates are available.

## 📄 License

See the [LICENSE](LICENSE) file for details.