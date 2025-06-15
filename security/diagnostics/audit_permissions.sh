#!/bin/bash

echo "[SECURITY] Auditing file permissions..."

find . -type f -perm /o+w -print | while read file; do
  echo "[!] Warning: World-writable file: $file"
done

find . -type d -perm /o+w -print | while read dir; do
  echo "[!] Warning: World-writable directory: $dir"
done
