from dataclasses import dataclass, field


# row format: comment_id|parent_id|author|text
rows = [
    "C-100|ROOT|Alice|Первый комментарий",
    "C-101|C-100|Bob|Ответ на первый",
    "C-102|C-100|Dina|Еще один ответ",
    "C-103|C-101|Max|Ответ второго уровня",
    "C-104|ROOT|Eva|Отдельная ветка",
    "C-105|C-104|Ira|Ответ в отдельной ветке",
    "C-106|C-103|Oleg|Третий уровень",
]


@dataclass
class CommentNode:
    comment_id: str
    author: str
    text: str
    children: list["CommentNode"] = field(default_factory=list)


def build_comment_tree(rows: list[str]) -> list[CommentNode]:
    # TODO 1: подготовить 2 словаря
    #   - nodes: comment_id -> CommentNode
    #   - parents: comment_id -> parent_id
    nodes:dict[str,CommentNode] = {}
    parents:dict[str,str] = {}


    # TODO 2: первый проход по rows
    #   - split строки по '|' на 4 части: comment_id, parent_id, author, text
    #   - создать CommentNode и положить в nodes
    #   - сохранить parent_id в parents
    for row in rows:
        comment_id, parent_id, author, text = row.split('|')
        nodes[comment_id] = CommentNode(comment_id, parent_id, author, text)
        parents[comment_id] = parents[parent_id]

        
    # TODO 3: второй проход по nodes
    #   - если parent_id == 'ROOT', добавить узел в список roots
    #   - иначе найти родителя в nodes[parent_id] и добавить текущий узел в parent.children
    roots:list[CommentNode] = list()
    for comment_id,node in nodes.items():
        parent_id = parents[comment_id]
        if parent_id == 'ROOT':
            roots.append(node)
        else:
            parent = nodes.get(parent_id)
            if parent is not None:
                parent.children.append(node)

    # TODO 4: вернуть roots
    return roots


def count_leaves(nodes: list[CommentNode]) -> int:
    # TODO 1: лист = узел без children
    # TODO 2: сделать вспомогательную функцию для одного узла:
    #   - если детей нет, вернуть 1
    #   - иначе вернуть сумму значений по всем детям
    # TODO 3: посчитать сумму этой функции для всех корневых узлов
    # TODO 4: вернуть итог
    leave = CommentNode()

    def node(node):
        


def max_depth(nodes: list[CommentNode]) -> int:
    # TODO 1: если roots пустой список, вернуть 0
    # TODO 2: сделать вспомогательную функцию depth_for_node(node):
    #   - если детей нет, вернуть 1
    #   - иначе вернуть 1 + максимум глубины среди детей
    # TODO 3: взять максимум depth_for_node(root) среди всех roots
    # TODO 4: вернуть этот максимум
    pass


def collect_paths(nodes: list[CommentNode]) -> list[list[str]]:
    # TODO 1: завести список paths для финальных путей
    # TODO 2: сделать вспомогательную функцию(node, current_path):
    #   - добавить node.comment_id в current_path
    #   - если это лист: добавить копию current_path в paths
    #   - иначе вызвать эту же функцию для каждого ребенка
    #   - после обхода убрать последний id из current_path
    # TODO 3: запустить вспомогательную функцию для каждого root
    # TODO 4: вернуть paths
    pass


roots = build_comment_tree(rows)

print("Корневых комментариев:", len(roots))
print("Листьев:", count_leaves(roots))
print("Максимальная глубина:", max_depth(roots))
print("Пути:")
for path in collect_paths(roots):
    print(path)
