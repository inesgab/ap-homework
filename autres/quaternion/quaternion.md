<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

## exercice - niveau avancé

Le [corps des quaternions](https://fr.wikipedia.org/wiki/Quaternion) est une extension non commutative du corps des complexes; la construction mathématique est totalement hors sujet pour nous, on va se contenter de ces quelques bribes :

* les quaternions peuvent être vus comme un espace vectoriel 
  sur $\mathbb{R}$, un peu comme les complexes mais de dimension 4
* un quaternion s'écrit donc $q = a + bi + cj + dk$  
  avec $(a, b, c, d) \in \mathbb{R}^4$  
  (les deux premiers éléments $1$ et $i$ de cette base canonique sont ceux des nombres complexes)
* les trois éléments $i, j, k$ sont tels que  
  $$i^2 = j^2 = k^2 = ijk = -1$$

**attention** : l'addition est bien commutative,  
mais à nouveau **la multiplication n'est pas commutative**  
ainsi par exemple $ij = k$ mais $ji = -k$

les règles indiquées ci-dessus impliquent (on vous laisse vous en assurer) que la table de multiplication est la suivante

![](media/quaternion-table.png)

On se propose ici d'écrire une classe pour représenter les quaternions.

**Notes importantes**

* il est malheureux que Python ait retenu la notation `j` pour représenter ce qu'on appelle $i$ dans le corps des complexes, surtout dans ce contexte des quaternions où il y a un autre nombre qui s'appelle justement $j$...

* le système de correction automatique a besoin également que votre classe définisse son comportement vis-à-vis de `repr()` ; regardez les exemples pour voir la représentation choisie, et inspirez-vous de la fonction `number_str` comme suit :


```python
# vous vous souvenez des type hints ?
# sinon retournez voir la semaine 4 séquence 1

def number_str(x: float) -> str:
    """
    la fonction utilisée dans Quaternion.__repr__ 
    pour la mise en forme des nombres
    """
    if isinstance(x, int):
        return f"{x}"
    elif isinstance(x, float):
        return f"{x:.1f}"
```


```python
from corrections.cls_quaternion import exo_quaternion
exo_quaternion.example()
```

*****


```python
# votre code

def ajouter_plus(chaine, coeff):
    if chaine != '':
        if coeff > 0:
            chaine += '+'

class Quaternion:
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
  
    def __repr__(self):
        result = ''
        if self.a != 0:
            result += number_str(self.a)
        if self.b != 0:
            ajouter_plus(result, self.b)
            result += number_str(self.b) + 'i'
        if self.c != 0:
            ajouter_plus(result, self.c)
            result += number_str(self.c) + 'j'
        if self.d != 0:
            ajouter_plus(result, self.d)
            result += number_str(self.d) + 'k'
        if result == '':
            return '0'
        return result
    
    def __add__(self, other):
        return Quaternion(self.a + other.a, self.b + other. b, self.c + other.c, self.d + other.d)
    
    
    def __mul__(self, other):
        a = self.a*other.a - self.b*other.b - self.c*other.c - self.d*other.d
        b = self.a*other.b + self.b*other.a - self.d*other.c + self.c*other.d
        c = self.a*other.c + self.c*other.a - self.b*other.d + self.d*other.b
        d = self.a*other.d + self.d*other.a - self.c*other.b + self.b*other.c
        return Quaternion(a, b, c, d)
        
```


```python
# correction
exo_quaternion.correction(Quaternion)
```

*****


```python
# peut-être utile pour debugger ?
I = Quaternion(0, 1, 0, 0)
J = Quaternion(0, 0, 1, 0)
K = Quaternion(0, 0, 0, 1)
```


```python
I*J == K
```


```python
J*K == I
```


```python
K*I == J
```


```python
I*I == J*J == K*K == -1
```


```python
J*K == 1j
```


```python
K*J == -1j
```


```python
Quaternion(1, 2, 3, 4) == (1+2j) + J * Quaternion(3-4j)
```


```python
...
```

comme exercice, vous pouvez aussi vous amuser à vérifier l'identité suivante (extraite de [cette vidéo de 3blue1brown](https://www.youtube.com/watch?v=d4EgbgTm0Bg))

![](media/quaternion-multiply.png)
