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
まずは新規登録  
<img width="911" alt="スクリーンショット 2021-02-04 093329" src="https://user-images.githubusercontent.com/73643164/106844998-496b8e80-66ed-11eb-80f6-5d906d8b4d19.png">  
そしてログイン  
<img width="911" alt="first" src="https://user-images.githubusercontent.com/73643164/106845090-86378580-66ed-11eb-8773-adf3f5dbfd13.png">  
トップページではまず服を追加するために、Add new clothを押す。  
<img width="1052" alt="add" src="https://user-images.githubusercontent.com/73643164/106845255-e9c1b300-66ed-11eb-9cf1-8bfdb0de89d6.png">  
フォームを満たして送信する。日付はカレンダー形式で入力できます。今回は例として[いらすとや](https://www.irasutoya.com/)から画像を引用しています。   
<img width="1066" alt="post" src="https://user-images.githubusercontent.com/73643164/106845403-386f4d00-66ee-11eb-9fbd-9f719ba71260.png">  
トップページでは、服の名前とブランド名と値段だけをテーブル上に表示されます。これはページネーションをすることができます。  
<img width="989" alt="paginaton2" src="https://user-images.githubusercontent.com/73643164/106845668-c51a0b00-66ee-11eb-967e-f0929febfe4c.png">  
これらは、購入日時が新しい順に表示されています。
<img width="1014" alt="pagination2" src="https://user-images.githubusercontent.com/73643164/106845698-d2cf9080-66ee-11eb-8d96-69d21a613674.png">  
服の詳細や服の編集、削除はdetailから見ることができます。服それぞれにdetailのボタンを押すことで詳細に飛べます。  
<img width="1052" alt="fordetail" src="https://user-images.githubusercontent.com/73643164/106845743-e975e780-66ee-11eb-90ad-64bd4ffba64e.png">  

<img width="952" alt="edit" src="https://user-images.githubusercontent.com/73643164/106845787-03172f00-66ef-11eb-9723-b87bcd9490cd.png">  
<img width="1025" alt="foredit" src="https://user-images.githubusercontent.com/73643164/106845809-0f02f100-66ef-11eb-9bfa-7e2958b67db9.png">  
<img width="952" alt="delete" src="https://user-images.githubusercontent.com/73643164/106845831-1aeeb300-66ef-11eb-91ef-ad2aa1831bfa.png">  
<img width="977" alt="fordelete" src="https://user-images.githubusercontent.com/73643164/106845855-27730b80-66ef-11eb-9497-7a9d06a8cf6c.png">  
<img width="1052" alt="search" src="https://user-images.githubusercontent.com/73643164/106845901-3bb70880-66ef-11eb-80c5-fb6e79887a8d.png">  
<img width="998" alt="search1" src="https://user-images.githubusercontent.com/73643164/106845934-483b6100-66ef-11eb-8b59-9577e3944e1c.png">  
<img width="989" alt="search2" src="https://user-images.githubusercontent.com/73643164/106845951-512c3280-66ef-11eb-9880-f8e08eb35aa4.png">  
<img width="1051" alt="seach3" src="https://user-images.githubusercontent.com/73643164/106846109-951f3780-66ef-11eb-97c8-db4413b2cd84.png">  
<img width="1052" alt="forwishlist" src="https://user-images.githubusercontent.com/73643164/106846137-a5371700-66ef-11eb-8f28-743b7d7ea9ba.png">  
<img width="1055" alt="wishlist" src="https://user-images.githubusercontent.com/73643164/106846171-b8e27d80-66ef-11eb-93a0-db1602409673.png">  
<img width="981" alt="add wishlist" src="https://user-images.githubusercontent.com/73643164/106846233-dca5c380-66ef-11eb-8087-32625ba1205f.png">  
<img width="1055" alt="wishlist pagination" src="https://user-images.githubusercontent.com/73643164/106846261-ec250c80-66ef-11eb-838c-6c03705a0ec2.png">  
<img width="1012" alt="wishlist pagination2" src="https://user-images.githubusercontent.com/73643164/106846295-f5ae7480-66ef-11eb-9051-49a4ebb02d8e.png">  
<img width="1034" alt="wishdetail" src="https://user-images.githubusercontent.com/73643164/106846359-11b21600-66f0-11eb-9523-3e0234b29ec1.png">  



























