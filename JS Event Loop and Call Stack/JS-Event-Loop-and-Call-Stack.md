## https://gist.github.com/jesstelford/9a35d20a2aa044df8bf241e00d7bc2d0


## VÒNG LẶP SỰ KIỆN JAVACRIPT (EVENT LOOP) VÀ CALL STACK LÀ GÌ ?
- VÒNG LẶP SỰ KIỆN BÌNH THƯỜNG (REGULAR EVENT LOOP) cho thấy thứ tự thực hiện được đưa ra cho CALL STACK JS, EVENT LOOP và bất kì APIs không đồng bộ nào cung cấp môi trường thực hiện JS ( Ví dụ : Web APIs trong một môi trường trình duyệt).

- Cho một đoạn code:

setTimeout(() => { 
  console.log('hi')
}, 1000)

- CALL STACK, EVENT LOOP và Web APIs sẽ hoạt động theo mối quan hệ sau:

- Đầu tiên mọi thứ hoàn toàn trống .

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
  setTimeout(() => {  |                   |              | |               |
    console.log('hi') |                   |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |

- Khi bắt đầu thực thi đoạn code và đẩy lên trên CALL STACK (ở đây sẽ là <global>).

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
  setTimeout(() => {  | <global>          |              | |               |
    console.log('hi') |                   |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |

- Sau đó hàm ( setTimeOut()) thực thi sẽ được đẩy vào call stack.

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
> setTimeout(() => {  | <global>          |              | |               |
    console.log('hi') | setTimeout        |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |

** Note: CALL STACK là một ngăn xếp, thứ vào sau sẽ được lấy ra trước (LAST IN, FIRST OUT : LIFO).

- Thực thi hàm setTimeOut() không phải là một phần của JS, Nó là một phần của Web APIs mà trình duyệt cung cấp cho chúng ta. 

- Sau khi thực thi setTimeOut() Web APIs sẽ đợi một khoảng thời gian được yêu cầu (1000ms).

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
> setTimeout(() => {  | <global>          |              | | timeout, 1000 |
    console.log('hi') | setTimeout        |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |

- Vì không còn dòng JS nào để thực thi, CALL STACK lúc này sẽ trống.

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
  setTimeout(() => {  |                   |              | | timeout, 1000 |
    console.log('hi') |                   |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |

- Sau khi hết thời gian chờ, Web APIs sẽ cho biết bằng cách thêm code vào vòng lặp sự kiện.

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
  setTimeout(() => {  |                   | function   <-----timeout, 1000 |
    console.log('hi') |                   |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |

- Nó sẽ không đẩy code trực tiếp về CALL STACK vì điều đó có thể gây lỗi.

- EVENT LOOP là một hàng chờ vào trước ra trước ( FIRST IN FIRST OUT : FIFO)

- Bất kể khi nào CALL STACK rỗng, môi trường thực thi JS sẽ kiểm tra xem có hàng chờ nào trong EVENT LOOP không. Nếu có , item đầu tiên trong EVENT LOOP được di chuyển sang CALL STACK để thực thi.

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
  setTimeout(() => {  | function        <---function     | |               |
    console.log('hi') |                   |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |

- Thực thi function này sẽ dẫn đến kết quả console.log được gọi và đẩy vào CALL STACK.

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
  setTimeout(() => {  | function          |              | |               |
>   console.log('hi') | console.log       |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |

- Sau khi thực thi xong, 'hi' được in ra và console.log được xoá khỏi CALL STACK

        [code]        |   [call stack]    | [Event Loop] | |   [Web APIs]  |
  --------------------|-------------------|--------------| |---------------|
  setTimeout(() => {  | function          |              | |               |
    console.log('hi') |                   |              | |               |
  }, 1000)            |                   |              | |               |
                      |                   |              | |               |
> hi

- Sau cùng, hàm không còn lệnh nào để thực thi, nó cũng sẽ bị đưa ra khỏi CALL STACK.

- Chương trình kết thúc.