# Queue

## 큐란?

큐(Queue)는 **먼저 넣은 데이터를 먼저 꺼내는** 선형 자료구조입니다. 이 규칙을 FIFO(First In, First Out)라고 합니다.

은행 창구의 대기 줄을 떠올리면 이해하기 쉽습니다. 새 사람은 줄의 뒤에 서고, 처리는 줄의 앞에 있는 사람부터 합니다. 큐에서 데이터를 꺼내는 앞쪽을 `front`, 넣는 뒤쪽을 `rear`라고 합니다.

```
front                         rear
  ↓                             ↓
[ A ] → [ B ] → [ C ] → [ D ]
```

위 큐에 `E`를 넣으면 `E`는 rear 뒤에 추가됩니다. 하나를 꺼내면 front의 `A`가 나옵니다.

## 핵심 연산

- `enqueue(x)`: `x`를 rear에 넣습니다.
- `dequeue()`: front 원소를 제거하고 반환합니다.
- `peek()` 또는 `front()`: front 원소를 제거하지 않고 확인합니다.
- `isEmpty()`: 큐가 비어 있는지 확인합니다.
- `size()`: 저장된 원소 수를 반환합니다.

연산 흐름은 다음과 같습니다.

```
Empty
enqueue(A) → [ A ]
enqueue(B) → [ A ][ B ]
enqueue(C) → [ A ][ B ][ C ]
dequeue()  → return A, [ B ][ C ]
peek()     → return B, [ B ][ C ]
```

비어 있는 큐에 `dequeue()`나 `peek()`를 호출하면 꺼낼 원소가 없습니다. 이를 **underflow(언더플로)** 라고 하며, 호출 전에 비어 있는지 확인해야 합니다.

## 추상 자료형과 구현

큐는 FIFO 규칙을 정의하는 **추상 자료형(ADT)** 입니다. 배열과 연결 리스트는 이 규칙을 실제 메모리에 구현하는 방법입니다.

### 배열 기반 구현: 원형 큐

배열로 큐를 구현할 때 앞쪽 원소를 꺼낸 뒤 나머지 원소를 모두 한 칸씩 앞으로 옮기면 `dequeue()`가 O(n)이 됩니다. 이를 피하려면 `front`와 `rear` 인덱스를 따로 두고, 배열의 끝에 도달하면 처음으로 돌아가는 **원형 큐(circular queue)** 를 사용합니다.

다음은 용량이 5인 빈 원형 큐입니다. `size`를 함께 저장하면 빈 상태와 가득 찬 상태를 명확히 구분할 수 있습니다.

```
index |  0  |  1  |  2  |  3  |  4  |
      +-----+-----+-----+-----+-----+
value |     |     |     |     |     |
      +-----+-----+-----+-----+-----+
front = 0, rear = 0, size = 0
```

`enqueue(A)`는 `rear` 위치에 `A`를 저장한 뒤 rear를 다음 칸으로 옮기고 size를 증가시킵니다. 이 구현에서 rear는 **다음에 삽입할 칸**을 가리킵니다.

```
1. array[rear] ← A
2. rear ← (rear + 1) mod 5
3. size ← size + 1

index |  0  |  1  |  2  |  3  |  4  |
      +-----+-----+-----+-----+-----+
value |  A  |     |     |     |     |
      +-----+-----+-----+-----+-----+
        ↑     ↑
      front  rear
front = 0, rear = 1, size = 1
```

`enqueue(B)`, `enqueue(C)`도 rear 위치에 추가합니다. front는 가장 먼저 꺼낼 `A`를 계속 가리킵니다.

```
index |  0  |  1  |  2  |  3  |  4  |
      +-----+-----+-----+-----+-----+
value |  A  |  B  |  C  |     |     |
      +-----+-----+-----+-----+-----+
        ↑                 ↑
      front              rear
front = 0, rear = 3, size = 3
```

`peek()`는 `array[front]`를 읽기만 합니다. 원소와 세 인덱스는 바뀌지 않습니다.

```
peek() → return A

index |  0  |  1  |  2  |  3  |  4  |
      +-----+-----+-----+-----+-----+
value |  A  |  B  |  C  |     |     |
      +-----+-----+-----+-----+-----+
        ↑                 ↑
      front              rear
```

`dequeue()`는 front 위치의 `A`를 기억하고 그 칸을 비운 뒤 front를 다음 칸으로 옮기며 size를 감소시킵니다. `B`, `C`를 앞으로 옮기지 않는 것이 원형 큐의 핵심입니다.

```
1. x ← array[front] = A
2. clear array[front]
3. front ← (front + 1) mod 5
4. size ← size - 1

index |  0  |  1  |  2  |  3  |  4  |
      +-----+-----+-----+-----+-----+
value |     |  B  |  C  |     |     |
      +-----+-----+-----+-----+-----+
              ↑           ↑
            front        rear
front = 1, rear = 3, size = 2

return A
```

이후 `enqueue(D)`, `enqueue(E)`, `enqueue(F)`를 수행하면 rear가 배열 끝을 넘어 0으로 돌아갑니다. 논리적인 큐 순서는 front부터 따라가야 하며, 배열에 보이는 순서와 항상 같지는 않습니다.

```
index |  0  |  1  |  2  |  3  |  4  |
      +-----+-----+-----+-----+-----+
value |  F  |  B  |  C  |  D  |  E  |
      +-----+-----+-----+-----+-----+
              ↑
        front, rear
front = 1, rear = 1, size = 5

logical order: B → C → D → E → F
```

`size = 0`이면 비어 있고, `size = capacity`이면 가득 찬 상태입니다. 따라서 `front = rear`여도 size가 0이면 빈 큐이고 size가 5이면 가득 찬 큐입니다.

```
isEmpty()
size = 0 → true
size > 0 → false

isFull()
size = 5 → true
size < 5 → false
```

- 장점: 원소가 연속된 메모리에 있어 접근이 빠르고, 미리 정한 용량 안에서는 메모리 사용량을 예측하기 쉽습니다.
- 주의: 고정 크기 배열은 가득 차면 overflow가 발생합니다. 동적 배열을 사용하더라도 원형 구조를 유지하면서 크기를 늘리는 처리가 필요합니다.

### 연결 리스트 기반 구현

연결 리스트 기반 큐는 첫 노드를 가리키는 `front`와 마지막 노드를 가리키는 `rear`를 모두 저장합니다. 각 노드는 값과 다음 노드를 가리키는 `next`를 함께 저장하며, 노드들이 연속된 메모리에 있을 필요는 없습니다.

빈 큐에서는 front와 rear가 모두 `null`입니다.

```
front → null
rear  → null
```

빈 큐에 `enqueue(A)`를 하면 새 노드가 첫 노드이자 마지막 노드가 됩니다. 따라서 front와 rear 모두 새 노드를 가리켜야 합니다.

```
new = [ A | null ]

front
  ↓
[ A | null ]
  ↑
rear
```

원소가 이미 있을 때 `enqueue(B)`, `enqueue(C)`는 기존 rear 노드의 next에 새 노드를 연결한 뒤 rear를 새 노드로 옮깁니다. front는 변하지 않습니다.

```
enqueue(B)
front                         rear
  ↓                             ↓
[ A |  • ] ───→ [ B | null ]

enqueue(C)
front                                       rear
  ↓                                           ↓
[ A |  • ] ───→ [ B |  • ] ───→ [ C | null ]
```

`peek()`는 front 노드의 값만 읽습니다. 연결 관계와 포인터는 바뀌지 않습니다.

```
peek() → return A

front                                       rear
  ↓                                           ↓
[ A |  • ] ───→ [ B |  • ] ───→ [ C | null ]
```

`dequeue()`는 front 노드의 값 `A`를 기억하고, front를 다음 노드로 옮깁니다. 이전 front 노드는 큐에서 분리됩니다.

```
1. x ← front.value = A
2. front ← front.next

front                         rear
  ↓                             ↓
[ B |  • ] ───→ [ C | null ]

3. return A
```

원소가 하나뿐인 큐에서 `dequeue()`를 하면 front가 `null`이 됩니다. 이때 rear도 반드시 `null`로 바꿔 빈 큐 상태를 유지해야 합니다.

```
before
front
  ↓
[ A | null ]
  ↑
rear

after dequeue()
front → null
rear  → null
```

연결 리스트는 새 노드를 만들 수 있는 한 삽입할 수 있으므로 고정 용량으로 인한 overflow는 없습니다. 다만 메모리가 부족하면 새 노드를 만들 수 없습니다. `size()`를 O(1)에 처리하려면 원소 수를 별도 변수로 저장하고 enqueue마다 증가, dequeue마다 감소시켜야 합니다.

- 장점: 미리 최대 크기를 정할 필요가 없습니다.
- 단점: 각 노드에 next 참조 공간이 추가로 필요하고, 원소가 흩어진 메모리에 있어 실제 실행에서는 배열보다 불리할 수 있습니다.

## 시간·공간 복잡도

| 연산 | 원형 배열 기반 | 연결 리스트 기반 | 이유 |
| --- | --- | --- | --- |
| `enqueue` | O(1) | O(1) | rear 위치 또는 rear 노드 하나만 변경합니다. |
| `dequeue` | O(1) | O(1) | front 위치 또는 front 노드 하나만 변경합니다. |
| `peek` | O(1) | O(1) | front 원소 하나만 확인합니다. |
| `isEmpty`, `size` | O(1) | O(1)·원소 수 저장 시 | 배열은 size를, 연결 리스트는 front와 저장한 원소 수를 확인합니다. |
| 전체 저장 공간 | O(n) | O(n) | 원소가 n개일 때 n개를 저장합니다. |

원형 배열의 복잡도는 배열 크기를 바꾸지 않는다는 전제에서 보장됩니다. 동적 배열을 확장하는 구현은 재배치 순간 O(n)이 들 수 있으며, 구현에 따라 `enqueue`의 상환 시간 복잡도가 O(1)이 됩니다.

## 의사코드

다음은 `front`, `rear`, `size`를 사용하는 원형 배열 큐의 의사코드입니다. `rear`는 다음에 삽입할 칸을 가리킵니다.

```
procedure ENQUEUE(Q, x)
    if Q.size = Q.capacity
        report overflow
    Q.array[Q.rear] ← x
    Q.rear ← (Q.rear + 1) mod Q.capacity
    Q.size ← Q.size + 1

procedure DEQUEUE(Q)
    if Q.size = 0
        report underflow
    x ← Q.array[Q.front]
    clear Q.array[Q.front]
    Q.front ← (Q.front + 1) mod Q.capacity
    Q.size ← Q.size - 1
    return x

procedure PEEK(Q)
    if Q.size = 0
        report underflow
    return Q.array[Q.front]

procedure IS_EMPTY(Q)
    return (Q.size = 0)
```

## Python

파이썬에서는 표준 라이브러리 `collections.deque`를 큐로 사용합니다. 양 끝에서 삽입과 제거를 O(1)에 처리하도록 설계되어 있으므로, `append()`와 `popleft()`가 큐의 `enqueue`, `dequeue`에 대응합니다.

```python
from collections import deque

queue = deque()

queue.append("A")
queue.append("B")

front = queue[0]
item = queue.popleft()

is_empty = not queue
size = len(queue)
```

`queue[0]`과 `queue.popleft()`는 큐가 비어 있으면 `IndexError`가 발생합니다. 따라서 빈 큐일 수 있는 경우에는 `if queue:`로 먼저 확인합니다. `list.pop(0)`은 남은 원소를 모두 앞으로 옮겨 O(n)이므로 일반적인 큐 구현에 사용하지 않습니다.

## 언제 쓰는가

큐는 먼저 도착한 작업을 먼저 처리해야 할 때 적합합니다.

- 작업 대기열: 프린터 작업, 서버 요청, 메시지 처리를 도착 순서대로 처리합니다.
- 너비 우선 탐색(BFS): 가까운 정점부터 차례대로 방문하기 위해 큐를 사용합니다. 이는 이후 그래프 탐색에서 다룹니다.
- 생산자·소비자 구조: 데이터를 만드는 쪽과 처리하는 쪽 사이에서 작업을 순서대로 전달합니다.
- 이벤트 처리: 입력이나 이벤트를 발생 순서대로 처리합니다.

## 자주 하는 실수

- 배열 큐에서 `dequeue()`할 때 남은 원소를 앞으로 모두 옮겨 O(n)이 되게 만듭니다.
- 원형 큐에서 rear를 이동할 때 나머지 연산을 빼먹어 배열 범위를 벗어납니다.
- `front = rear`만으로 빈 상태와 가득 찬 상태를 구분하려 합니다. size를 저장하거나 한 칸을 비워 두는 규칙이 필요합니다.
- 연결 리스트 큐에서 마지막 원소를 꺼낸 뒤 rear를 `null`로 바꾸지 않습니다.
- 큐의 실제 저장 위치와 front부터의 논리적 순서를 혼동합니다.

## 핵심 정리

큐는 front에서 제거하고 rear에서 삽입해 FIFO를 보장합니다. 배열 큐는 원형 인덱스를 사용해야 앞쪽 삭제를 O(1)에 처리할 수 있고, 연결 리스트 큐는 front와 rear를 모두 저장해야 양쪽 연산을 O(1)에 처리할 수 있습니다.
