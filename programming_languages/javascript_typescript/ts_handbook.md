# TypeScript 📘🔵

Inicialmente, a linguagem JavaScript foi criada para atender um demanda "pequena", isto é, para escrever poucas linhas de código no client-side, por isso ela é muito simples. No entanto, com o decorrer do tempo, sua popularidade e sua abrangência cresceram, e a linguagem passou a ser utilizada também no server-side, por exemplo. Com isso, houve a necessidade de aprimorar certos aspectos do JavaScript que poderiam causar bugs complexos, então surgiu o TypeScript.

## Introdução

![Logo TypeScript](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIrOXd86iDXx-hL8ZoHFwV7SR5ihBzQcvOgg&s)

[Documentação do TypeScript](https://www.typescriptlang.org/docs): as informações presentes neste documento são majoritariamente retiradas da documentação oficial, que, felizmente, é muito bem arranjada e acessível tanto para desenvolvedores mais experientes, quanto para desenvolvedores iniciantes. Ela será utilizada como referência principal ao longo da pesquisa sobre TypeScript, uma vez que é a fonte mais confiável e completa.

Tipos determinam tanto o comportamente da leitura quanto da escrita. Nesse sentido, JS é uma linguagem fracamente tipada, por isso surgiu o TS, para permitir que os devs adicionem tipos aos dados em JavaScript.

Há duas formas de atribuir tipos em TS:
- Explicit: escrevendo (demarcando) o nome do tipo. EX: `let firstName: string = "Soraya";`. É mais intuitivo e fácil de ler.
- Implicit: o TS precisa adivinhar que tipo é. EX: `let firstName = "Soraya";`. O tipo do valor é chamado INFER, porque ele faz uma inferência.
- Entretanto, nem sempre o TS faz inferência do tipo, atribuindo `any`, o que pode ser alterado no arquivo de configuração do TS (tsconfig.json).

Para definir os tipos dos atributos de um objeto, é necessário criar uma `interface` antes, como demonstrado a seguir. As interfaces podem ser extendidades com a palavra-chave `extends` e são utilizadas para objetos e assinaturas de funções.

```typescript

    interface Sorvete {
        sabor: string;
        preço: number;
        id: number;
    };

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

#### Compilação e Transpilação:

- Transpilação é realizar a conversão do código de uma linguagem para outra linguagem.
- O processo de compilação realiza uma transpilação do código TypeScript para JavaScript.

------------
## TypeScript Handbook 🖐️📙

Geralmente, erros que surgem na programação em JavaScript puro estão relacionados a erros de tipo, quando um certo tipo de valor foi usado em um local que recebe outro tipo de valor. Nesse sentido, o intuito do TypeScript é fazer uma verificação estáticas dos tipos em programas JavaScript.

O TypeScript Handbook pretende ser uma documentação de fácil compreensão para o dia a dia dos devs. Alguém que completa sua leitura deve ser capaz de ler e assimilar padrões e sintaxe do TypeScript, explicar os efeitos de diferentes opções de compiladores e prever o comportamento dos tipos.

#### The Basics

---
#### Everyday Types
- *Unit types* são subtipos dos tipos primitivos que contêm estritamente um valor primitivo. É como dizer que a string "foo" tem o tipo "foo". 


[**Literal Types**](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-types), em tradução livre, são tipos literais. É quando o tipo do elemento é seu próprio valor; pode-se dizer que é uma constante mais que constante. Há o tipo `boolean` que possui dois literal types: `true` ou `false`.

Por exemplo: `let x: "hello" = "hello";`. Isso não é muito útil por si só, todavia ao combinar vários tipos em uma onion, o leque de possibilidades se abre. Tal como, é possível criar uma função que aceita apenas valores específicos como parâmetro.

```typescript
function compare(a: string, b: string): -1 | 0 | 1 {
  return a === b ? 0 : a > b ? 1 : -1;
}
```

----
#### Narrowing

----
#### More on Functions

---
#### Object Types

- Objetos em JS são uma forma de agrupar e passar dados. Seu tipo pode ser definido com `interface` ou `type` alias:
```typescript
// Agora é possível testar o código separadamente no Jupyter, de forma prática.
// Utilize o arquivo jupyter.ipynb

type Person = {
    name: string;
    age: number;
};

function greet(person: Person) {
    //return "Hello " + person.name;
    return `Hello ${person.name}`;
}

const soraya: Person = {
    name: "Soraya",
    age: 19
}
console.log(greet(soraya));
```
- Para indicar um atributo opcional, basta colocar um `?` na frente do nome da variável.
```typescript
type Person = {
    name: string;
    age: number;
    address?: string | undefined;
};
```
- JavaScript também suporta a passagem de parâmetro padrão para a assinatura de uma função. A sintaxe é igual a do Python. 
- Há a possibilidade de declarar um tipo vazio. O atributo `{k: 10}` tem todas as propriedades de Empty { } por que Empty não tem propriedades!

```typescript
class Empty {}

function fn(arg: Empty) {
  // do something?
}
 
// No error, but this isn't an 'Empty' ?
fn({ k: 10 });
```

-----
#### Type Manipulation

------
#### Creating Types from Types

-----
#### Generics
[Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) compõem uma estrutura que facilita a reusabilidade de código, por meio da abstração de tipos.

Podem ser utilizados em interfaces, classes e funções. Sendo assim, uma função que aceita um argumento genérico aceita qualquer tipo de dado naquele argumento; uma classe com atributo genérico aceita qualquer tipo de dado no atributo genérico; e uma interface genérica aceita qualquer tipo. Ao contrário do tipo `any`, o Generics permite o conhecimento do tipo inserido em cada caso.

```typescript

export interface Generic<T>  {
    (arg1: T, arg2: T): T;
}

const sum: Generic<number> = (arg1, arg2) => {
    return arg1+arg2;
};
sum(1, 2);

export interface setStorage<T> {
    set(key: string, value: T): void;
}

const array = [1, 2, 2, 3, 3, 4, 4];
removeDuplicates(array);

export function removeDuplicates<T>(array: T[]): T[] {
    const uniqueSet = new Set<T>(array);
    return Array.from(uniqueSet);
}

```

-----
#### Keyof Type Operator

----
#### Typeof Type Operator

-------
#### Indexed Access Types

------
#### Conditional Types

-----
#### Mapped Types

------
#### Template Literal Types

------
#### Classes Modules