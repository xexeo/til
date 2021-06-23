# O diálogo

Um exemplo em html está em (ConversacomTópicos.html)[ConversacomTópicos.html]

## Criando os links

Em uma sala que rode no início do jogo, coloque o seguinte código:

```
<!-- Funcao que cria os links -->
(set: $dtmtalk to (macro: str-type _ps , array-type _opts ,
[(output-data: (joined: ", " , ...(altered: _op via '(link: "'+_op+'")[(set: $__option to "'+_op+'")(goto: "'+_ps+'")]' , ..._opts)))]))
```

## Fazendo a conversa
A ideia é que você começa com apenas um pouco de opções, mas a medida que vai conversando, aumenta essas opções.
A estrutura é a seguinte: a variável $bartender guarda um datamap, que é uma espécie de lista na forma chave/conteúdo.
Essa código pode ficar em qualquer lugar antes do próximo código

```
(set: $bartender to
(datamap:
"castle", (a: "Ah, lord Appleby rules there", (a: "lord appleby"), ""),
"smithing", (a: "My brother is the best smith in the town", (a: "brother"), ""),
"soldiers", (a: "They keep the bandits away", (a: "bandits"), ""),
"brother", (a: "The best blacksmith in town", (a:), ""),
"lord appleby", (a: "He does a fairly good job of ruling", (a:), ""),
"bandits", (a: "Used to cause all kinds of trouble for the traders, but the soldiers keep them in check now.", (a: "soldiers", "traders"), ""),
"traders", (a: "They come through here every week peddling their wares.", (a:), ""),
"end", (a: "Be off with you now. I have a business to run", (a:), ""),
"unknown", (a: "I don't know much about that", "You'll have to ask someone else", "Who knows?"))
)
```

Além disso você precisa de criar a lista de tópicos iniciais para essa conversa:

```
(set: $topics_bartender to (a: "castle", "smithing", "soldiers"))
```

Cada conteúdo é uma array (a:), como 4 itens: um texto que responde à chave, uma array com a nova chave e um item vazio (isso é modificado pelo programa mais tarde)

## Antes da conversando
Antes de ir para a conversa, você deve ter um código preparando a conversa
O importante são os 4 set: que serão usados na conversa

```
O Balcão do Caixa tem, no momento, uma pessoa cuidando dele. Você vê Carla, que está embrulhando um jogo que um cliente acaba de comprar para presente.
Você quer falar com Carla?
O Caixa fica na [[Recepção->Recepção]].
(set: $topics to $topics_bartender)
(set: $__conv to $bartender)
(set: $__option to "castle")
(set: $__endpassage to "leave_bar")
Você pode [[falar com a responsável pela caixa->Conversa com a caixa]]:
````

## A conversa

Fazer uma sala só para a conversando
Esse é um exemplo



```
<!-- can this be macrofied? -->
<!-- since it changes $topics, I am not sure -->
{(unless: $__option is "")[
  (if: $__conv contains $__option)[
	  (set: $__response to $__conv's $__option)
	  (print: $__response's 1st)
	  (print: $__response's 3rd)
	  (set: $topics to $topics - $__response's 2nd)
	  (set: $topics to $__response's 2nd + $topics)]
  (else:)[(print: (either: ... $__conv's unknown))]]}

You can ask about the following:

($dtmtalk: "Conversa com a caixa" , $topics)

Or you can (link-repeat: "end the conversation")[
(print: $__conv's end's 1st)
(print: $__conv's end's 3rd)
[[chega de conversa->Caixa]]
]
```
