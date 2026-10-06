# Câu hỏi và trả lời luyện bảo vệ khóa luận

Tổng hợp vòng luyện tập đầu tiên gồm 10 câu hỏi. Mỗi mục giữ ý trả lời ban đầu của em (đã chỉnh lỗi gõ), câu trả lời đề xuất và điểm cần tránh. Câu trả lời đề xuất dùng để luyện diễn đạt, không phải bổ sung kết quả thí nghiệm mới.

Các số kết quả được trình bày với bốn chữ số sau dấu thập phân. Chênh lệch được lấy từ kết quả trước khi làm tròn, không tính lại từ các điểm đã làm tròn. “Unseen data” chỉ dữ liệu không dùng cho training và selection; nếu kết quả đã được xem trước thì phải nói rõ giới hạn đó.

## 1. Khóa luận giải quyết vấn đề gì và vì sao đáng nghiên cứu?

**Câu hỏi:** Trong 60–90 giây, em hãy giải thích khóa luận giải quyết vấn đề gì trong truy xuất văn bản pháp luật tiếng Việt, và vì sao vấn đề đó đáng nghiên cứu. Chưa cần kể tên model hay thuật toán.

**Ý trả lời ban đầu:** Chưa có benchmark cụ thể cho văn bản luật tiếng Việt, chưa có cách tối ưu truy hồi. Khóa luận thử kết hợp ba model theo vector và keyword để đo hiệu quả.

**Trả lời đề xuất:**

> Khóa luận của em nghiên cứu cách truy xuất đúng điều khoản pháp luật tiếng Việt cho một câu hỏi. Khó khăn là các văn bản có nội dung gần nhau, nhưng điều khoản cùng chủ đề chưa chắc cung cấp thông tin cần thiết để trả lời. Cách diễn đạt của người hỏi cũng có thể khác với câu chữ trong luật.
>
> Em đánh giá việc kết hợp lexical và semantic retrieval trên ALQAC, Zalo và bộ dữ liệu BCA. Các thí nghiệm kiểm tra hybrid có cải thiện so với BM25 không, thêm E5 có mang lại giá trị không, và fine-tuning BGE-M3 có cải thiện toàn bộ hệ thống trên unseen data không. Phạm vi nghiên cứu là chất lượng truy xuất điều khoản, không phải chất lượng câu trả lời do hệ thống sinh ra.

**Điểm cần tránh:**

- Không nói “chưa có benchmark”, vì luận văn sử dụng ALQAC và Zalo.
- Không khẳng định tìm được cách tối ưu cho mọi corpus.
- Dùng “chất lượng truy xuất” nếu chưa đo tốc độ hoặc tài nguyên.
- BM25 là phương pháp lexical retrieval; BGE-M3 và multilingual-E5-base là hai mô hình embedding.

## 2. Vì sao kết hợp BM25 với BGE-M3 có thể tốt hơn dùng riêng?

**Câu hỏi:** Vì sao kết hợp BM25 với BGE-M3 có thể tốt hơn dùng riêng từng phương pháp? Hãy đưa một ví dụ câu hỏi pháp luật để giải thích vai trò của lexical và semantic retrieval.

**Ý trả lời ban đầu:** BM25 tìm chính xác theo keyword, BGE tìm theo ngữ nghĩa; hai phương pháp bù đắp nhau. Ví dụ: “Lái xe ngược chiều phạt bao nhiêu?”.

**Trả lời đề xuất:**

> BM25 chấm điểm dựa trên mức khớp từ giữa query và tài liệu. BGE-M3 dùng biểu diễn ngữ nghĩa, nên có thể giúp kết nối những cách diễn đạt khác nhau. Hai tín hiệu có thể bổ sung nhau, nhưng lợi ích phải được kiểm chứng bằng thí nghiệm.
>
> Ví dụ minh họa là câu hỏi “Đi xe máy ngược chiều bị phạt bao nhiêu?”. BM25 tận dụng các từ xuất hiện trực tiếp như “xe máy”, “ngược chiều”. BGE-M3 có thể giúp liên hệ cách hỏi đời thường với cách diễn đạt khác trong văn bản luật. Cả hai retriever xử lý cùng câu hỏi, không phải mỗi phương pháp xử lý một phần riêng của câu.

**Điểm cần tránh:**

- Khớp keyword không bảo đảm tìm đúng điều khoản.
- “Ngược chiều” cũng có thể là keyword của BM25.
- BM25 không tự kiểm tra hiệu lực pháp luật theo năm.
- Ví dụ trên giải thích cơ chế dự kiến, không phải kết quả truy xuất đã được đo hoặc kết luận về mức phạt.

## 3. Điểm được chuẩn hóa, kết hợp và chọn trọng số thế nào?

**Câu hỏi:** Trong hệ thống, điểm BM25 và BGE-M3 được chuẩn hóa và kết hợp thế nào? Trọng số được chọn trên dữ liệu nào để tránh dùng kết quả đánh giá cuối cùng cho việc lựa chọn?

**Ý trả lời ban đầu:** Dùng trọng số, thử nhiều bước để tìm trọng số tối ưu; chia test data và dữ liệu đánh giá riêng để bảo đảm công bằng.

**Trả lời đề xuất:**

> Điểm BM25 và điểm dense có thang đo khác nhau. Em dùng min–max để chuẩn hóa riêng điểm từng retriever theo mỗi query trên toàn corpus, rồi cộng các điểm đã chuẩn hóa với trọng số không âm và tổng bằng một.
>
> Trong baseline, em thử grid trọng số với bước 0.1. Ở mỗi fold, phần dữ liệu chọn trọng số được dùng để tìm cấu hình có mean NDCG@10 cao nhất trong grid. Sau đó em khóa trọng số và đánh giá trên fold còn lại, không dùng nhãn của fold đánh giá để lựa chọn.
>
> Các query được nhóm theo thành phần liên thông của các luật tham chiếu để giảm nguy cơ rò rỉ do những câu hỏi có chung luật nằm ở cả hai phía. BCA có giao thức riêng cho giant component và các small components.

**Điểm cần tránh:**

- Nói “tốt nhất trong grid đã thử”, không nói “tối ưu toàn cục”.
- Phân biệt dữ liệu chọn trọng số với dữ liệu đánh giá; “test data và đánh giá data” không làm rõ hai vai trò.
- Không mô tả baseline như chia ngẫu nhiên từng query.
- Tách baseline khỏi giao thức riêng của các nghiên cứu fine-tuning.

## 4. Vì sao chọn NDCG@10 thay vì chỉ dùng Hit@10?

**Câu hỏi:** Vì sao NDCG@10 là metric chính? Nó phản ánh điều gì mà Hit@10 không phản ánh được?

**Ý trả lời ban đầu:** Chưa rõ. Với câu hỏi phụ về Hit@10 giữ nguyên nhưng NDCG@10 giảm, em trả lời rằng độ chính xác kém hơn.

**Trả lời đề xuất:**

> Em chọn NDCG@10 vì mục tiêu là đưa các điều khoản liên quan lên đầu danh sách, không chỉ tìm thấy chúng trong top 10. NDCG@10 thưởng nhiều hơn cho tài liệu liên quan ở vị trí cao và chuẩn hóa theo thứ tự lý tưởng của các nhãn liên quan.
>
> Hit@10 của luận văn chỉ ghi nhận query có ít nhất một điều khoản được gán nhãn liên quan trong top 10 hay không. Ví dụ, khi chỉ có một mục tiêu liên quan, đặt nó ở vị trí 1 hoặc vị trí 10 đều tạo ra hit, nhưng NDCG@10 khác nhau.

**Câu hỏi phụ:** Nếu Hit@10 giữ nguyên nhưng NDCG@10 giảm, em diễn giải thế nào?

> Tỷ lệ query tìm thấy ít nhất một mục tiêu trong top 10 không đổi, nhưng chất lượng xếp hạng theo NDCG@10 giảm. Điều khoản liên quan có thể bị đẩy xuống thấp hơn hoặc việc thu hồi các mục tiêu liên quan khác có thể thay đổi. Hit@10 bằng nhau không bảo đảm cùng những query có hit; hệ thống có thể mất hit ở query này và thêm hit ở query khác.

**Điểm cần tránh:** Không gọi chung là “độ chính xác giảm”. Hãy nói đúng loại chất lượng mà metric đo: chất lượng xếp hạng.

## 5. Thêm E5 có luôn cải thiện BM25+BGE-M3 không?

**Câu hỏi:** Kết quả có cho thấy thêm E5 luôn tốt hơn không? Điều kiện nào cải thiện rõ nhất và nên rút ra kết luận gì?

**Ý trả lời ban đầu:** Thêm E5 không cải thiện so với BM25+BGE-M3; sau fine-tuning cũng chưa có cải thiện rõ ràng.

**Trả lời đề xuất:**

> Thêm E5 không luôn cải thiện kết quả. Với pretrained baseline, ALQAC clean và parsed có NDCG@10 giảm nhẹ. Zalo clean tăng rất nhỏ, còn Zalo parsed-with-fallback có cải thiện rõ nhất: từ 0.7214 lên 0.7344, với chênh lệch được báo cáo là +0.0130.
>
> Vì vậy, giá trị bổ sung của E5 phụ thuộc dataset và điều kiện corpus. Không thể mặc định nhiều retriever hơn sẽ tốt hơn. BCA cũng chưa thiết lập được lợi thế E5 đáng tin cậy trong phân tích small-component.

**Các số cần nhớ:**

- ALQAC clean: delta NDCG@10 = -0.0021.
- ALQAC parsed: delta NDCG@10 = -0.0012.
- Zalo clean: delta NDCG@10 = +0.0013.
- Zalo parsed-with-fallback: delta NDCG@10 = +0.0130.

**Điểm cần tránh:** Không trộn phép so sánh thêm E5 với phép so sánh pretrained và fine-tuned BGE-M3 trong cùng hybrid. Đây là hai can thiệp khác nhau.

## 6. Vì sao development cải thiện nhưng hybrid giảm trên unseen data?

**Câu hỏi:** Fine-tuning BGE-M3 cải thiện trên development nhưng hybrid giảm trên unseen data. Đâu là kết luận được dữ liệu chứng minh, đâu chỉ là giả thuyết?

**Ý trả lời ban đầu:** Development cải thiện chưa rõ; model có vẻ học thuộc development thay vì được cải tiến.

**Trả lời đề xuất:**

> Trong Study A, cấu hình được chọn cải thiện development NDCG@10 là +0.0609 ở hybrid hai thành phần và +0.0689 ở hybrid ba thành phần. Nhưng cải thiện đó không chuyển sang unseen data: delta trung bình lần lượt là -0.0520 và -0.0249.
>
> Kết luận được hỗ trợ là recipe này chưa chứng minh được lợi ích cho hybrid trên unseen data theo giao thức hiện tại. Khả năng khái quát của recipe hoặc sự phù hợp của trọng số fusion là những giải thích có thể kiểm tra thêm, chưa phải nguyên nhân đã được chứng minh.
>
> Kết quả corrected evaluation là post-hoc vì một phân tích sơ bộ đã từng xem fold đánh giá. Dữ liệu không dùng cho training và selection, nhưng không phải một tập test hoàn toàn chưa từng được xem kết quả.

**Điểm cần tránh:**

- Development dùng để chọn cấu hình trong pilot, không trực tiếp cập nhật model; không khẳng định “học thuộc development”.
- Khoảng tin cậy của các chênh lệch trong corrected evaluation chứa zero. Không nói fine-tuning đã được chứng minh gây hại ở cấp độ quần thể.
- Không nói fine-tuning luôn thất bại: Study B có cải thiện dense-only.

## 7. Vì sao dense-only tốt hơn nhưng hybrid chưa tốt hơn?

**Câu hỏi:** Vì sao BGE-M3 dùng riêng có thể cải thiện sau fine-tuning, nhưng hybrid với BM25 không cải thiện tương ứng?

**Ý trả lời ban đầu:** Các query BM25 xử lý tốt thì BGE kém hơn, làm trung hòa điểm số.

**Trả lời đề xuất:**

> Hybrid cần các tín hiệu bổ sung nhau, nên cải thiện của một retriever dùng riêng không bảo đảm cải thiện hệ thống kết hợp. BGE-M3 có thể cải thiện ở những query mà BM25 đã xử lý tốt, nên lợi ích bổ sung ít. Đồng thời, thay đổi điểm của BGE-M3 có thể làm giảm chất lượng thứ tự kết hợp ở các query khác.
>
> Trọng số được chọn cho pretrained BGE-M3 cũng có thể không còn phù hợp với điểm sau fine-tuning. Đây là các giả thuyết, vì thí nghiệm chưa tách riêng các cơ chế đó. Kết quả trực tiếp là Study B cải thiện dense-only nhưng không tạo ra lợi ích hybrid đạt ngưỡng thực tiễn đã đặt ra khi dùng trọng số khóa.

**Điểm cần tránh:** BM25 truy xuất và xếp hạng, không sinh câu trả lời. Không khẳng định “BM25 tốt thì BGE kém” cho toàn bộ query nếu chưa có phân tích chứng minh.

## 8. Mục tiêu không có trong corpus ảnh hưởng đánh giá BCA thế nào?

**Câu hỏi:** Vì sao cần báo cáo cả toàn bộ query và nhóm có ít nhất một mục tiêu trong corpus?

**Ý trả lời ban đầu:** Một số câu hỏi không có câu trả lời nên thuật toán luôn sai, ảnh hưởng đánh giá.

**Trả lời đề xuất:**

> Vấn đề không phải câu hỏi không có câu trả lời, mà là mục tiêu được gán nhãn không được biểu diễn trong corpus. Nếu không có mục tiêu nào trong corpus, mọi retriever đều không thể thu hồi mục tiêu đó bằng cách thay đổi thứ tự xếp hạng.
>
> Kết quả trên toàn bộ query phản ánh cả độ bao phủ corpus và chất lượng xếp hạng. Nhóm có ít nhất một mục tiêu trong corpus giúp đánh giá truy xuất khi có bằng chứng để tìm. Báo cáo cả hai tránh quy mọi thất bại cho thuật toán hoặc che giấu giới hạn dữ liệu.
>
> Nhóm này vẫn gồm các query chỉ có một phần mục tiêu trong corpus, nên không đồng nghĩa mọi bằng chứng liên quan đều sẵn có.

**Các số cần nhớ:** BCA có 546 query đánh giá; 440 có ít nhất một mục tiêu được biểu diễn, 106 không có mục tiêu được biểu diễn. Trong 440 query đó, 229 là các trường hợp thiếu một phần mục tiêu. Không cộng 229 như một nhóm độc lập với 440.

## 9. Đóng góp là gì khi các thuật toán đều đã có?

**Câu hỏi:** BM25, BGE-M3, E5 và weighted fusion đều đã có. Vậy đóng góp của khóa luận là gì?

**Ý trả lời ban đầu:** Đo các chỉ số trên các dataset sử dụng và tạo thêm một dataset thực tế có thể sử dụng.

**Trả lời đề xuất:**

> Khóa luận không đề xuất thuật toán mới. Đóng góp chính là đánh giá có kiểm soát các cấu hình retrieval trên các bộ dữ liệu pháp luật tiếng Việt và điều kiện corpus khác nhau.
>
> Kết quả cho thấy hybrid cải thiện so với BM25 trong các điều kiện được báo cáo, nhưng thêm E5 không luôn có lợi. Fine-tuning cải thiện dense retriever cũng không bảo đảm cải thiện toàn bộ hybrid. Các kết quả này giúp xác định giới hạn của việc bổ sung model và thích nghi encoder.
>
> Em còn xây dựng BCA từ câu hỏi thực tế và trích dẫn trong câu trả lời công khai, đồng thời phân tích độ bao phủ mục tiêu và sự phụ thuộc giữa các query khi đánh giá.

**Điểm cần tránh:** Không chỉ nói “chạy model và đo chỉ số”. Không gọi BCA là benchmark hoàn chỉnh với nhãn liên quan đầy đủ nếu chưa được thẩm định độc lập. Nhãn được suy ra từ trích dẫn, có thể thiếu bằng chứng liên quan hoặc có mục tiêu chưa được biểu diễn trong corpus.

## 10. Thí nghiệm tiếp theo nên ưu tiên gì?

**Câu hỏi:** Đề xuất một thí nghiệm để làm rõ vì sao fine-tuning cải thiện dense-only nhưng chưa cải thiện hybrid. So sánh cấu hình nào, chọn tham số trên dữ liệu nào và đánh giá trên dữ liệu nào?

**Ý trả lời ban đầu:** Thử cải thiện three-way, thay model khác và áp dụng đầy đủ pipeline để tối ưu kết quả.

**Trả lời đề xuất:**

> Em ưu tiên kiểm tra liệu trọng số fusion chọn cho pretrained BGE-M3 còn phù hợp sau fine-tuning hay không. Em giữ nguyên corpus, query, BM25, E5 và cách chuẩn hóa, rồi so sánh ba cấu hình:
>
> 1. Pretrained BGE-M3 với trọng số chọn cho pretrained, làm baseline.
> 2. Fine-tuned BGE-M3 với trọng số pretrained giữ nguyên, để đo tác động thay encoder.
> 3. Fine-tuned BGE-M3 với trọng số chọn lại trên development, để kiểm tra điều chỉnh fusion.
>
> Em khóa các cấu hình sau selection và đánh giá trên cùng một tập mới, không dùng cho training hoặc selection và chưa từng xem kết quả. Nếu chọn lại trọng số cải thiện kết quả, điều đó hỗ trợ giả thuyết rằng cấu hình fusion ảnh hưởng đến khả năng chuyển lợi ích dense-only sang hybrid, nhưng chưa chứng minh đây là nguyên nhân duy nhất.

**Điểm cần tránh:** Đây là đề xuất nghiên cứu tiếp theo, không phải thí nghiệm đã hoàn thành. Thay model, thêm reranking và thay pipeline cùng lúc sẽ khó xác định thành phần nào tạo ra thay đổi.

## Những điểm cần ôn trước buổi bảo vệ

- Giải thích được min–max, grid trọng số và ranh giới training/selection/evaluation.
- Phân biệt Hit@10 với NDCG@10; dùng đúng thuật ngữ chất lượng xếp hạng.
- Nhớ E5 có lợi rõ nhất ở Zalo parsed-with-fallback, không phải hoàn toàn không cải thiện.
- Phân biệt Study A với Study B, dense-only với hybrid và development với unseen data.
- Tách kết quả quan sát được khỏi giả thuyết nguyên nhân.
- Nêu giới hạn post-hoc evaluation và nhãn BCA khi có câu hỏi liên quan.
- Đề xuất thí nghiệm thay một yếu tố, giữ các yếu tố khác cố định.

## Chỗ đối chiếu trong bản thảo

- `chapters/chapter_4.tex`: chuẩn hóa, fusion grid, grouped evaluation và giao thức training/selection.
- `chapters/chapter_5.tex`: bảng incremental E5, development selection, corrected unseen-data evaluation, Study B và BCA coverage.
- `chapters/chapter_2.tex` và `chapters/chapter_3.tex`: bối cảnh nghiên cứu và định nghĩa metric/phương pháp.
