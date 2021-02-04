# Close Cloth-服管理アプリ-
## リンク
[Close Cloth](http://13.231.147.58/clothes/)  
テスト用アカウント  
ユーザー名: fortest  
パスワード: kimutes9876　　
## 概要
Close Clothは服をまるで図鑑のように管理することができるアプリです。
## 詳細
自分の持っている服を追加して管理することができます。購入場所や購入日や値段、ブランド名といったような情報を付与できます。また、服に今までいくら使ったかを計算します。これに加えて、ブランド名、購入場所、服の種類で検索をかけることができます。これにより、自分がどのような服やブランド、お店を気に入っているかが一目瞭然になります。
## 機能一覧
・ユーザーの新規登録  
・ユーザーのログイン  
・服の追加(これは、PostgreSQL上にデータが保管されます。このリポジトリのコード内では、開発環境であるDjangoのデフォルトであるsqliteになっています。また、Nginxとgunicornを連携し、それをEC2で作成したUbuntuのインスタンスを仮想マシンとして扱っているため、1MB以上の画像をアップロードすることができません。)    
・服の情報の編集  
・服の情報の削除  
・服の検索(購入場所、ブランド名、服の種類で検索をかけることができます。その購入場所、ブランド、服の種類の総数、それぞれの値段の合計が分かります。)  
・WishListの追加(WishListは優先度を1から3の3段階に設定できます。優先度1が最優先で、優先度3が一番優先度が低いです。WishListの一覧では優先度が高い順に表示されます。)  
・WishListの情報の編集  
・WishListの情報の削除  
・服とWishListの一覧はどちらもページネーション可能。
## デモ

