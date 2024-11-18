# TypeScript 📘🔵

Inicialmente, a linguagem javascript foi criada para atender um demanda "pequena", isto é, para escrever poucas linhas de código no client-side, por isso ela é muito simples. No entanto, com o decorrer do tempo, sua popularidade e sua abrangência cresceram, e a linguagem passou a ser utilizada também no server-side, por exemplo. Com isso, houve a necessidade de aprimorar certos aspectos do javascript que poderiam causar bugs complexos, então surgiu o TypeScript.

## Introdução

![Logo TypeScript](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIrOXd86iDXx-hL8ZoHFwV7SR5ihBzQcvOgg&s)

JS é uma linguagem fracamente tipada. Então, o TS surgiu para permitir que os devs adicionem tipos aos dados em javascript.

Há duas formas de atribuir tipos em TS:
- Explicit: escrevendo (demarcando) o nome do tipo. EX: `let firstName: string = "Soraya";`. É mais intuitivo e fácil de ler.

- Implicit: o TS precisa adivinhar que tipo é. EX: `let firstName = "Soraya";`. O tipo do valor é chamado INFER, porque ele faz uma inferência.

- Entretanto, nem sempre o TS faz inferência do tipo, atribuindo `any`, o que pode ser alterado no arquivo de configuração do TS (tsconfig.json).

Para definir os tipos dos atributos de um objeto, é necessário criar uma `interface` antes, como demonstrado a seguir.

```typescript

    interface Sorvete {
        sabor: string;
        preço: number;
        id: number;
    }

    const sorvete: Sorvete = {
        sabor: "Açaí",
        preco: 30.0,
        id: 0,
    };
```
Para o caso de declarar classes, é muito parecido.

```typescript
    class Sorvete {
        sabor: string;
        preco: number;
        id: number;

        constructor(sabor: string, preco: number, id: number) {
            this.sabor = sabor;
            this.preco = preco;
            this.id = id;
        }
    }
    
    const sorvete: Sorvete = new Sorvete("Açaí", 30.0, 0);
```

Declarando funções:

```typescript

    function comerSorvete(sorvete: Sorvete): void {
        //
    }
```

Os tipos primitivos em TypeScript são: boolean, bigint, null, number, string, symbol, undefined, any, unknown, never, void, object.

Outros tipos:

|Tipo|Explicação|
|----------|----------|
|unknown|tipo superior|
|never|tipo inferior|
|object literal|ex. { property: Type }|
|void|para funções sem retorno documentado|
|T[]|vetor mutável, também escrito como <T>|
|[T, T]|tuplas, que têm tamanho fixo, mas mutável|
|(t: T) => U|funções. Ex.: `let fst: (a: any, b: any) => any = (a, b) => a;`|


- É possível criar novos tipos combinando os primitivos. Há duas formas, com `unions` e `generics`.

- Há como escrever uma função que retorna determinados resultados de acordo com o tipo do parâmetro que foi passado.

- Um tipo, em TS, é um conjunto de valores que compartilham algo em comum. 

- Há a possibilidade de declarar um tipo vazio. O atributo `{k: 10}` tem todas as propriedades de Empty { } por que Empty não tem propriedades!

```typescript
class Empty {}
 
function fn(arg: Empty) {
  // do something?
}
 
// No error, but this isn't an 'Empty' ?
fn({ k: 10 });
```

- *Unit types* são subtipos dos tipos primitivos que contêm estritamente um valor primitivo. É como dizer que a string "foo" tem o tipo "foo". 


-------------------------
*Sobre Paradigmas de Programação*, [vídeo](https://youtu.be/sqKnYS-ZXsQ?si=Ep64J9IPRHdxeoTl):
- Imperativos: Programação Procedural, Programação Orientada a Objetos.
- Declarativos: Programação Funcional, Programação Lógica.

*Programação Funcional*: existem linguagens puramente funcionais, como Closure, OCamel Haskell e Lisp. 

------------------