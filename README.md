# chuikyo-notify
Notify when there is an update on the Chuikyo website

## Overview

Checking for update on the Chuikyo website every day at 10am, 2pm, 6pm (JST) using GitHub Actions.<br>
If there is an update, notify with LINE Notify.

![chuikyo-notify](https://github.com/ssatocc/chuikyo-notify/assets/153752928/895f29b7-36da-4585-81d0-7d2d255934d1)

### LINE Notify

<img src="https://github.com/ssatocc/chuikyo-notify/assets/153752928/274ed308-fb86-48a0-8e05-a48e022b9eb6" width="463px">

## GitHub Pages

Display the latest number saved by batch workflow.

- [ssatocc.github.io/chuikyo-notify/](https://ssatocc.github.io/chuikyo-notify/)

## Chuikyo website

- [中央社会保険医療協議会(中央社会保険医療協議会総会) ｜ 厚生労働省](https://www.mhlw.go.jp/stf/shingi/shingi-chuo_128154.html)
- [利用規約・リンク・著作権等 ｜ 厚生労働省](https://www.mhlw.go.jp/chosakuken/index.html)

## Repository secrets

- ACCESS_TOKEN
  - Access token (LINE Notify)
  - No expiration
- PAT
  - Personal access token (GitHub)
  - Expires on `Thu, Feb 20 2025`

## Docs

- [LINE Notify](https://notify-bot.line.me/ja/)
- [Creating a fine-grained personal access token | GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)
