# Close Cloth-服管理アプリ-
## リンク
※現在はサーバーを停止しています。再度サーバーを立て直そうと検討しています。  
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
・服の追加(これは、PostgreSQL上にデータが保管されます。このリポジトリのコード内では、開発環境であるDjangoのデフォルトであるsqliteになっています。また、webサーバーとしてNginxを用いている都合上、1MB以上の画像をアップロードすることができません。)    
・服の情報の編集  
・服の情報の削除  
・服の検索(購入場所、ブランド名、服の種類で検索をかけることができます。その購入場所、ブランド、服の種類の総数、それぞれの値段の合計が分かります。)  
・WishListの追加(WishListは優先度を1から3の3段階に設定できます。優先度1が最優先で、優先度3が一番優先度が低いです。WishListの一覧では優先度が高い順に表示されます。)  
・WishListの情報の編集  
・WishListの情報の削除  
・服とWishListの一覧はどちらもページネーション可能。
## デモ&使い方
まずは新規登録  
<img width="911" alt="スクリーンショット 2021-02-04 093329" src="https://user-images.githubusercontent.com/73643164/106844998-496b8e80-66ed-11eb-80f6-5d906d8b4d19.png">  
そしてログイン。今回はfortestのアカウントでログインしています。  
<img width="911" alt="first" src="https://user-images.githubusercontent.com/73643164/106845090-86378580-66ed-11eb-8773-adf3f5dbfd13.png">  
トップページではまず服を追加するために、Add new clothを押します。  
<img width="1052" alt="add" src="https://user-images.githubusercontent.com/73643164/106845255-e9c1b300-66ed-11eb-9cf1-8bfdb0de89d6.png">  
フォームを満たして送信する。日付はカレンダー形式で入力できます。今回は例として[いらすとや](https://www.irasutoya.com/)から画像を引用しています。   
<img width="1066" alt="post" src="https://user-images.githubusercontent.com/73643164/106845403-386f4d00-66ee-11eb-9fbd-9f719ba71260.png">  
トップページでは、服の名前とブランド名と値段だけをテーブル上に表示されます。これはページネーションをすることができます。  
<img width="989" alt="paginaton2" src="https://user-images.githubusercontent.com/73643164/106845668-c51a0b00-66ee-11eb-967e-f0929febfe4c.png">  
これらは、購入日時が新しい順に表示されています。
<img width="1014" alt="pagination2" src="https://user-images.githubusercontent.com/73643164/106845698-d2cf9080-66ee-11eb-8d96-69d21a613674.png">  
服の詳細や服の編集、削除はdetailから見ることができます。服それぞれにdetailのボタンを押すことで詳細に飛べます。  
<img width="1052" alt="fordetail" src="https://user-images.githubusercontent.com/73643164/106845743-e975e780-66ee-11eb-90ad-64bd4ffba64e.png">  
このような画面が表示されます。ここでは画像と服の詳細を見ることができます。編集をしたい場合はeditのボタンを押します。  
<img width="952" alt="edit" src="https://user-images.githubusercontent.com/73643164/106845787-03172f00-66ef-11eb-9723-b87bcd9490cd.png">  
編集したい内容をフォーム上に入力し、editのボタンを押すことで内容を変更することができます。押した後は、トップページに戻ります。  
<img width="1025" alt="foredit" src="https://user-images.githubusercontent.com/73643164/106845809-0f02f100-66ef-11eb-9bfa-7e2958b67db9.png">  
削除をしたい場合は、詳細の画面からdeleteのボタンを押します。
<img width="952" alt="delete" src="https://user-images.githubusercontent.com/73643164/106845831-1aeeb300-66ef-11eb-91ef-ad2aa1831bfa.png">  
削除する服の情報を確認し、削除するので問題がなければdeleteのボタンを押します。押した後は、こちらもトップページに戻ります。  
<img width="977" alt="fordelete" src="https://user-images.githubusercontent.com/73643164/106845855-27730b80-66ef-11eb-9497-7a9d06a8cf6c.png">  
服をブランドや購入場所、種類で絞り込むことができます。それをしたいときは、searchボタンを押します。  
<img width="1052" alt="search" src="https://user-images.githubusercontent.com/73643164/106845901-3bb70880-66ef-11eb-80c5-fb6e79887a8d.png">  
検索画面では、フォームに検索したい内容を入力し、searchボタンを押します。  
<img width="998" alt="search1" src="https://user-images.githubusercontent.com/73643164/106845934-483b6100-66ef-11eb-8b59-9577e3944e1c.png">  
まずサンプルとしてブランドをサンプル1とサンプル2を用意してあります。そのため、サンプル1とフォームに入力してみました。結果として3つの情報が返ってきました。このように、そのブランドごとの合計金額を確認することが可能です。また、ここからも詳細に飛ぶことができます。  
<img width="989" alt="search2" src="https://user-images.githubusercontent.com/73643164/106845951-512c3280-66ef-11eb-9880-f8e08eb35aa4.png">  
次に、服の種類としてtopsを指定しました。結果として4つの情報が返ってきました。ここでも種類ごとの合計金額を確認できます。
<img width="1051" alt="seach3" src="https://user-images.githubusercontent.com/73643164/106846109-951f3780-66ef-11eb-97c8-db4413b2cd84.png">  
WishListはトップページからWishListのボタンを押すことで移動できます。
<img width="1052" alt="forwishlist" src="https://user-images.githubusercontent.com/73643164/106846137-a5371700-66ef-11eb-8f28-743b7d7ea9ba.png">  
WishListも服の追加と同様の手順で追加できます。WishListのトップからadd WishListを押します。
<img width="1055" alt="wishlist" src="https://user-images.githubusercontent.com/73643164/106846171-b8e27d80-66ef-11eb-93a0-db1602409673.png">  
こちらでもフォームを満たしてaddを押します。
<img width="981" alt="add wishlist" src="https://user-images.githubusercontent.com/73643164/106846233-dca5c380-66ef-11eb-8087-32625ba1205f.png">  
こちらもページネーションが可能です。WishListは優先度順に表示されます。優先度は3段階あり、優先度１は赤色、優先度2は黄色、優先度3は黒色で表示されます。
<img width="1055" alt="wishlist pagination" src="https://user-images.githubusercontent.com/73643164/106846261-ec250c80-66ef-11eb-838c-6c03705a0ec2.png">  
このように、優先度3は優先度が低いため、次のページに表示されます。また、予想価格の合計を確認することができます。
<img width="1012" alt="wishlist pagination2" src="https://user-images.githubusercontent.com/73643164/106846295-f5ae7480-66ef-11eb-9051-49a4ebb02d8e.png">  
WishListもdetailボタンを押すことで詳細に飛ぶことができます。
<img width="1034" alt="wishdetail" src="https://user-images.githubusercontent.com/73643164/106846359-11b21600-66f0-11eb-9523-3e0234b29ec1.png">  
WishListのdetailも服のdetailとできることは同じです。
<img width="707" alt="wishwish" src="https://user-images.githubusercontent.com/73643164/106861635-5d24ee00-6709-11eb-94b3-4f7964290785.png">  
## 注意点
機能一覧にも書きましたが、画像ファイルが1MBを超えるとNginxからエラーがでるのでそれ以下のファイルを送信するようにしてください。




























