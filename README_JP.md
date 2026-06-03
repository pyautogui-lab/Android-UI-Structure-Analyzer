# Android UI Structure Analyzer

🇺🇸 English documentation: README.md

AndroidスタイルのUI XML構造を解析し、UI要素の情報を抽出するPython製の技術検証プロジェクトです。

## 概要

本ツールは、resource-id を用いてUI要素を検索し、bounds（座標範囲）情報を抽出して中心座標を計算します。

Android UIレイアウトの構造理解や、UI解析技術の学習を目的として開発しました。

## 主な機能

* XMLレイアウトの解析
* resource-idによるUI要素検索
* bounds情報の抽出
* UI要素の中心座標計算

## 使用技術

* Python 3
* 正規表現（re）
* Dataclasses
* XML解析

## 実行結果例

[1] resource-id: sample.app:id/target_button
bounds: (120, 450) - (300, 520)
center: (210, 485)

[2] resource-id: sample.app:id/target_button
bounds: (400, 800) - (580, 870)
center: (490, 835)

## このプロジェクトで学んだこと

* 正規表現を用いた構造化データの抽出
* dataclassを利用したデータ管理
* XMLデータの解析手法
* 座標計算ロジックの実装
* Pythonによる小規模ツール開発
* デバッグによる問題解決の進め方

開発中、対象のUI要素が検出できない問題が発生しました。調査の結果、Pythonの正規表現における `.` がデフォルトでは改行にマッチしないことが原因であると判明しました。

この問題は `re.DOTALL` を利用することで解決でき、正規表現の挙動やデバッグの重要性について理解を深めることができました。

## 開発背景

本リポジトリは、個人的に実施したAndroid UI解析の技術検証を、公開用に簡略化・一般化したものです。

元のプロトタイプでは、Android端末上のTermux環境およびUIAutomatorを利用し、UIレイアウト情報の取得や座標抽出を行っていました。

公開版では、特定アプリや端末環境への依存を避けるため、サンプルXMLを利用した構成に変更しています。

これにより、Python環境のみで動作確認できる形に整理しています。
