#!/usr/bin/env bash
vagrant up db --provider=aws
vagrant up webapp background-job --provider=aws
