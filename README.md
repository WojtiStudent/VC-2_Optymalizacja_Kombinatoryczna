# Pokrycie_wierzcho-kowe_s-siad-w_1szego_i_2giego_rz-du
====== Projekt ======

Wojciech Spychalski, Agata Szpotek

**Temat: Problem pokrycia (VC) - pokrycie sąsiadów pierwszego i 2-rzędu.** $VC^{(2)}$

===== Streszczenie =====
Autorzy projektu zaprojektowali i zaimplementowali algorytm pełnego przeglądu podzbiorów wierzchołków grafu, które pokrywają sąsiednie wierzchołki zarówno 1 jak i 2 rzędu. W artykule zawarty jest algorytm sprawdzający pokrycie danego podzbioru, generujący zbiór potęgowy zbioru wierzchołków grafu oraz procedura wykonująca pełen przegląd grafu. Oprócz algorytmów znajduje się tutaj również wizualizacja problemu przy pomocy macierzy oraz oprogramowania generującego grafy GraphViz, a także wykresy związane z średnim czasem wykonania przeglądu oraz średnią wielkością pokrywającego graf podzbioru wierzchołków.


** Słowa kluczowe: ** 
  *[[https://pl.wikipedia.org/wiki/Pokrycie_wierzcho%C5%82kowe|Pokrycie wierzchołkowe]] (ang. //vertex cover//)
  *[[https://en.wikipedia.org/wiki/Neighbourhood_(graph_theory)|Sąsiedztwo]]
  *[[https://en.wikipedia.org/wiki/Second_neighborhood_problem]]

===== Wprowadzenie =====

===== Definicja =====
Problem $VC^{(2)}$ jest uogólnieniem klasycznego problemu pokrycia wierzchołkowego $VC^{(1)}$ z tą różnicą, że w tym przypadku zasięg pokrycia grafu przez jeden wierzchołek jest rozszerzony z pokrycia sąsiednich wierzchołków (**sąsiadów pierwszego rzędu**) do pokrycia sąsiednich wierzchołków oraz ich sąsiednich wierzchołków (**sąsiadów drugiego rzędu**). W obu przypadkach szukamy rozwiązania w którym wybrane wierzchołki są w stanie pokryć wszystkie wierzchołki znajdujące się w grafie.

===== Analiza średniej złożoności =====

** Pytanie **: Przy jakich wartościach $p$ w modelu $G(n,p)$ oczekiwana liczba wierzchołków należących do rozwiązania równa się 1, 2, 3. 

** Przypadek graniczny: ** Jeżeli $p=1.0$ wówczas w modelu $G(n,p)$ losowany jest graf pełny $K_n$. Dla grafu $K_n$ optymalnym rozwiązaniem problemu $VC^{(2)}$ jest wybór jednego (dowolnego) z jego wierzchołków. 

** Pozostałe przypadki: ** Wykres średniej wielkość zbioru pokrywającego graf dla założonych prawdopodobieństw $p=0.25,0.50,0.75$ został umieszczony w dziale **Wykresy średniej wielkości dobrego zbioru (takiego, który pokrywa graf)**

==== Wykresy opisujące złożoność ====

Wykresy te opisują stosunek czasu wykonania (w sekundach) ''Pełnego przeglądu grafu'' dla $G_n$ do czasu wykonania (w sekundach) ''Pełnego przeglądu grafu ''$G_\frac{n}{2}$ $f(\frac{t(n)}{t(\frac{n}{2})})$, gdzie $n$ to liczba wierzchołków w grafie, dla każdego z założonych prawdopodobieństw $p=0.25,0.50,0.75$:

=== Wykres dla p = 0.25 ===

{{ :ok20:pr013:p145392:t25.png?400 |}}

=== Wykres dla p = 0.50 ===

{{ :ok20:pr013:p145392:t50.png?400 |}}

=== Wykres dla p = 0.75 ===

{{ :ok20:pr013:p145392:t75.png?400 |}}

Przebieg tych wykresów wskazuje na ewidentną złożoność czasową **wykładniczą, bądź wyższą**.
===== Lasy i drzewa =====
Legenda do ilustracji znajduje się w dziale **Ilustracja Problemu**.
==== Ścieżki ====
Jeden wierzchołek przy ścieżce bez rozgałęzień pokrywa do 5 wierzchołków (licząc razem ze sobą).

//Pokrycie// $P_5$ // przy pomocy jednego wierzchołka // 
<svg width="377pt" height="33pt"
 viewBox="0.00 0.00 566.00 44.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 40)">
<title>%3</title>
<polygon fill="white" stroke="none" points="-4,4 -4,-40 562,-40 562,4 -4,4"/>
<!-- 0 -->
<g id="node1" class="node"><title>0</title>
<ellipse fill="none" stroke="black" cx="27" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">0</text>
</g>
<!-- 1 -->
<g id="node2" class="node"><title>1</title>
<ellipse fill="none" stroke="black" cx="153" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="153" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">1</text>
</g>
<!-- 0&#45;&#45;1 -->
<g id="edge1" class="edge"><title>0&#45;&#45;1</title>
<path fill="none" stroke="yellow" d="M54.0302,-18C75.1448,-18 104.366,-18 125.58,-18"/>
</g>
<!-- 2 -->
<g id="node3" class="node"><title>2</title>
<ellipse fill="none" stroke="green" cx="279" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="279" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">2</text>
</g>
<!-- 1&#45;&#45;2 -->
<g id="edge2" class="edge"><title>1&#45;&#45;2</title>
<path fill="none" stroke="green" d="M180.03,-18C201.145,-18 230.366,-18 251.58,-18"/>
</g>
<!-- 3 -->
<g id="node4" class="node"><title>3</title>
<ellipse fill="none" stroke="black" cx="405" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="405" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">3</text>
</g>
<!-- 2&#45;&#45;3 -->
<g id="edge3" class="edge"><title>2&#45;&#45;3</title>
<path fill="none" stroke="green" d="M306.03,-18C327.145,-18 356.366,-18 377.58,-18"/>
</g>
<!-- 4 -->
<g id="node5" class="node"><title>4</title>
<ellipse fill="none" stroke="black" cx="531" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="531" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">4</text>
</g>
<!-- 3&#45;&#45;4 -->
<g id="edge4" class="edge"><title>3&#45;&#45;4</title>
<path fill="none" stroke="yellow" d="M432.03,-18C453.145,-18 482.366,-18 503.58,-18"/>
</g>
</g>
</svg>


Do optymalnego pokrycia takiej ścieżki potrzeba $\lceil n/5 \rceil$ wierzchołków.


//Próba pokrycia// $P_6$ // przy pomocy jednego wierzchołka // 
<svg width="461pt" height="33pt"
 viewBox="0.00 0.00 692.00 44.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 40)">
<title>%3</title>
<polygon fill="white" stroke="none" points="-4,4 -4,-40 688,-40 688,4 -4,4"/>
<!-- 0 -->
<g id="node1" class="node"><title>0</title>
<ellipse fill="none" stroke="black" cx="27" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">0</text>
</g>
<!-- 1 -->
<g id="node2" class="node"><title>1</title>
<ellipse fill="none" stroke="black" cx="153" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="153" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">1</text>
</g>
<!-- 0&#45;&#45;1 -->
<g id="edge1" class="edge"><title>0&#45;&#45;1</title>
<path fill="none" stroke="yellow" d="M54.0302,-18C75.1448,-18 104.366,-18 125.58,-18"/>
</g>
<!-- 2 -->
<g id="node3" class="node"><title>2</title>
<ellipse fill="none" stroke="green" cx="279" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="279" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">2</text>
</g>
<!-- 1&#45;&#45;2 -->
<g id="edge2" class="edge"><title>1&#45;&#45;2</title>
<path fill="none" stroke="green" d="M180.03,-18C201.145,-18 230.366,-18 251.58,-18"/>
</g>
<!-- 3 -->
<g id="node4" class="node"><title>3</title>
<ellipse fill="none" stroke="black" cx="405" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="405" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">3</text>
</g>
<!-- 2&#45;&#45;3 -->
<g id="edge3" class="edge"><title>2&#45;&#45;3</title>
<path fill="none" stroke="green" d="M306.03,-18C327.145,-18 356.366,-18 377.58,-18"/>
</g>
<!-- 4 -->
<g id="node5" class="node"><title>4</title>
<ellipse fill="none" stroke="black" cx="531" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="531" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">4</text>
</g>
<!-- 3&#45;&#45;4 -->
<g id="edge4" class="edge"><title>3&#45;&#45;4</title>
<path fill="none" stroke="yellow" d="M432.03,-18C453.145,-18 482.366,-18 503.58,-18"/>
</g>
<!-- 5 -->
<g id="node6" class="node"><title>5</title>
<ellipse fill="none" stroke="red" cx="657" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="657" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">5</text>
</g>
<!-- 4&#45;&#45;5 -->
<g id="edge5" class="edge"><title>4&#45;&#45;5</title>
<path fill="none" stroke="black" d="M558.03,-18C579.145,-18 608.366,-18 629.58,-18"/>
</g>
</g>
</svg>




==== Drzewa i Lasy ====

Jest to rozszerzona wersja ścieżki $P_n$ - w tym wypadku występują rozgałęzienia. Aby optymalnie pokryć graf każdy wierzchołek nie będący w zbiorze rozwiązań musi być oddalony od wierzchołka pochodzącego z takiego zbioru o maksymalnie 2 krawędzie.

//Próba pokrycia// $T_{10}$ // przy pomocy jednego wierzchołka // 

<svg width="243pt" height="219pt"
 viewBox="0.00 0.00 365.19 329.01" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(210.091 194.911)">
<title>%3</title>
<polygon fill="white" stroke="none" points="-210.091,134.102 -210.091,-194.911 155.104,-194.911 155.104,134.102 -210.091,134.102"/>
<!-- 0 -->
<g id="node1" class="node"><title>0</title>
<ellipse fill="none" stroke="green" cx="18.0118" cy="-14.3106" rx="27" ry="18"/>
<text text-anchor="middle" x="18.0118" y="-10.6106" font-family="Times New Roman,serif" font-size="14.00">0</text>
</g>
<!-- 1 -->
<g id="node2" class="node"><title>1</title>
<ellipse fill="none" stroke="black" cx="67.2676" cy="54.2946" rx="27" ry="18"/>
<text text-anchor="middle" x="67.2676" y="57.9946" font-family="Times New Roman,serif" font-size="14.00">1</text>
</g>
<!-- 0&#45;&#45;1 -->
<g id="edge1" class="edge"><title>0&#45;&#45;1</title>
<path fill="none" stroke="green" d="M29.6847,1.94786C37.4227,12.7256 47.5459,26.8256 55.3363,37.6763"/>
</g>
<!-- 3 -->
<g id="node4" class="node"><title>3</title>
<ellipse fill="none" stroke="black" cx="-44.8983" cy="-63.3175" rx="27" ry="18"/>
<text text-anchor="middle" x="-44.8983" y="-59.6175" font-family="Times New Roman,serif" font-size="14.00">3</text>
</g>
<!-- 0&#45;&#45;3 -->
<g id="edge2" class="edge"><title>0&#45;&#45;3</title>
<path fill="none" stroke="green" d="M0.152558,-28.2229C-8.42041,-34.9013 -18.6618,-42.8793 -27.2122,-49.54"/>
</g>
<!-- 4 -->
<g id="node5" class="node"><title>4</title>
<ellipse fill="none" stroke="black" cx="36.2978" cy="-97.4226" rx="27" ry="18"/>
<text text-anchor="middle" x="36.2978" y="-93.7226" font-family="Times New Roman,serif" font-size="14.00">4</text>
</g>
<!-- 0&#45;&#45;4 -->
<g id="edge3" class="edge"><title>0&#45;&#45;4</title>
<path fill="none" stroke="green" d="M21.9796,-32.3447C25.0468,-46.2854 29.2725,-65.492 32.3378,-79.4238"/>
</g>
<!-- 6 -->
<g id="node7" class="node"><title>6</title>
<ellipse fill="none" stroke="black" cx="95.6426" cy="-29.2646" rx="27" ry="18"/>
<text text-anchor="middle" x="95.6426" y="-25.5646" font-family="Times New Roman,serif" font-size="14.00">6</text>
</g>
<!-- 0&#45;&#45;6 -->
<g id="edge4" class="edge"><title>0&#45;&#45;6</title>
<path fill="none" stroke="green" d="M44.294,-19.3734C52.4756,-20.9494 61.4894,-22.6857 69.651,-24.2579"/>
</g>
<!-- 7 -->
<g id="node8" class="node"><title>7</title>
<ellipse fill="none" stroke="black" cx="-50.2659" cy="33.9999" rx="27" ry="18"/>
<text text-anchor="middle" x="-50.2659" y="37.6999" font-family="Times New Roman,serif" font-size="14.00">7</text>
</g>
<!-- 0&#45;&#45;7 -->
<g id="edge5" class="edge"><title>0&#45;&#45;7</title>
<path fill="none" stroke="green" d="M-0.645388,-1.10956C-10.2795,5.70713 -22.0005,14.0004 -31.6313,20.8148"/>
</g>
<!-- 2 -->
<g id="node3" class="node"><title>2</title>
<ellipse fill="none" stroke="black" cx="124.104" cy="107.348" rx="27" ry="18"/>
<text text-anchor="middle" x="124.104" y="111.048" font-family="Times New Roman,serif" font-size="14.00">2</text>
</g>
<!-- 1&#45;&#45;2 -->
<g id="edge6" class="edge"><title>1&#45;&#45;2</title>
<path fill="none" stroke="yellow" d="M83.0996,69.0729C90.9827,76.4313 100.485,85.3012 108.356,92.6487"/>
</g>
<!-- 5 -->
<g id="node6" class="node"><title>5</title>
<ellipse fill="none" stroke="black" cx="51.6179" cy="-172.911" rx="27" ry="18"/>
<text text-anchor="middle" x="51.6179" y="-169.211" font-family="Times New Roman,serif" font-size="14.00">5</text>
</g>
<!-- 4&#45;&#45;5 -->
<g id="edge7" class="edge"><title>4&#45;&#45;5</title>
<path fill="none" stroke="yellow" d="M39.9285,-115.312C42.3529,-127.258 45.5302,-142.914 47.9602,-154.888"/>
</g>
<!-- 8 -->
<g id="node9" class="node"><title>8</title>
<ellipse fill="none" stroke="black" cx="-118.686" cy="69.482" rx="27" ry="18"/>
<text text-anchor="middle" x="-118.686" y="73.182" font-family="Times New Roman,serif" font-size="14.00">8</text>
</g>
<!-- 7&#45;&#45;8 -->
<g id="edge8" class="edge"><title>7&#45;&#45;8</title>
<path fill="none" stroke="yellow" d="M-71.9145,45.2267C-79.9011,49.3685 -88.9486,54.0604 -96.9435,58.2065"/>
</g>
<!-- 9 -->
<g id="node10" class="node"><title>9</title>
<ellipse fill="none" stroke="red" cx="-179.091" cy="112.102" rx="27" ry="18"/>
<text text-anchor="middle" x="-179.091" y="115.802" font-family="Times New Roman,serif" font-size="14.00">9</text>
</g>
<!-- 8&#45;&#45;9 -->
<g id="edge9" class="edge"><title>8&#45;&#45;9</title>
<path fill="none" stroke="black" d="M-137.467,82.7336C-144.81,87.914 -153.208,93.8395 -160.529,99.0049"/>
</g>
</g>
</svg>


==== Drzewa binarne ====

Dla zbalansowanych drzew (wysokość pomiędzy gałęziami różni się maksymalnie o 1) oby optymalnie pokryć graf wystarczy do zbioru rozwiązania dodać wszystkie wierzchołki z co 5 poziomu wysokości( 2 pierwsze poziomy pokrywa 1 aktualny poziom rozwiązujący, następne 2 następny poziom rozwiązujący), najlepiej rozpoczynając o 2 poziomu (korzeń ma poziom 0). Należy również wziąć pod uwagę, że ostatni poziom należący do rozwiązania nie może być oddalony o więcej niż 2 poziomy od ostatniego poziomu wysokości drzewa.


//Pokrycie// $BT_{31}$ // przy pomocy jednego poziomu wierzchołków // 
<svg width="650pt" height="180pt"
 viewBox="0.00 0.00 1142.00 332.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 328)">
<title>BST</title>
<polygon fill="white" stroke="none" points="-4,4 -4,-328 1138,-328 1138,4 -4,4"/>
<!-- l0 -->
<g id="node1" class="node"><title>l0</title>
<ellipse fill="none" stroke="black" cx="567" cy="-306" rx="27" ry="18"/>
<text text-anchor="middle" x="567" y="-302.3" font-family="Arial" font-size="14.00">0</text>
</g>
<!-- l1 -->
<g id="node2" class="node"><title>l1</title>
<ellipse fill="none" stroke="black" cx="423" cy="-234" rx="27" ry="18"/>
<text text-anchor="middle" x="423" y="-230.3" font-family="Arial" font-size="14.00">1</text>
</g>
<!-- l0&#45;&gt;l1 -->
<g id="edge1" class="edge"><title>l0&#45;&gt;l1</title>
<path fill="none" stroke="yellow" d="M545.752,-294.671C521.398,-282.832 481.281,-263.331 453.572,-249.862"/>
<polygon fill="yellow" stroke="yellow" points="454.859,-246.595 444.335,-245.371 451.798,-252.891 454.859,-246.595"/>
</g>
<!-- l2 -->
<g id="node3" class="node"><title>l2</title>
<ellipse fill="none" stroke="black" cx="711" cy="-234" rx="27" ry="18"/>
<text text-anchor="middle" x="711" y="-230.3" font-family="Arial" font-size="14.00">2</text>
</g>
<!-- l0&#45;&gt;l2 -->
<g id="edge2" class="edge"><title>l0&#45;&gt;l2</title>
<path fill="none" stroke="yellow" d="M588.248,-294.671C612.602,-282.832 652.719,-263.331 680.428,-249.862"/>
<polygon fill="yellow" stroke="yellow" points="682.202,-252.891 689.665,-245.371 679.141,-246.595 682.202,-252.891"/>
</g>
<!-- l3 -->
<g id="node4" class="node"><title>l3</title>
<ellipse fill="none" stroke="green" cx="207" cy="-162" rx="27" ry="18"/>
<text text-anchor="middle" x="207" y="-158.3" font-family="Arial" font-size="14.00">3</text>
</g>
<!-- l1&#45;&gt;l3 -->
<g id="edge3" class="edge"><title>l1&#45;&gt;l3</title>
<path fill="none" stroke="green" d="M399.059,-225.241C360.438,-212.725 284.285,-188.046 240.363,-173.812"/>
<polygon fill="green" stroke="green" points="241.311,-170.44 230.719,-170.687 239.153,-177.099 241.311,-170.44"/>
</g>
<!-- l4 -->
<g id="node5" class="node"><title>l4</title>
<ellipse fill="none" stroke="green" cx="423" cy="-162" rx="27" ry="18"/>
<text text-anchor="middle" x="423" y="-158.3" font-family="Arial" font-size="14.00">4</text>
</g>
<!-- l1&#45;&gt;l4 -->
<g id="edge4" class="edge"><title>l1&#45;&gt;l4</title>
<path fill="none" stroke="green" d="M423,-215.697C423,-207.983 423,-198.712 423,-190.112"/>
<polygon fill="green" stroke="green" points="426.5,-190.104 423,-180.104 419.5,-190.104 426.5,-190.104"/>
</g>
<!-- l5 -->
<g id="node6" class="node"><title>l5</title>
<ellipse fill="none" stroke="green" cx="711" cy="-162" rx="27" ry="18"/>
<text text-anchor="middle" x="711" y="-158.3" font-family="Arial" font-size="14.00">5</text>
</g>
<!-- l2&#45;&gt;l5 -->
<g id="edge5" class="edge"><title>l2&#45;&gt;l5</title>
<path fill="none" stroke="green" d="M711,-215.697C711,-207.983 711,-198.712 711,-190.112"/>
<polygon fill="green" stroke="green" points="714.5,-190.104 711,-180.104 707.5,-190.104 714.5,-190.104"/>
</g>
<!-- l6 -->
<g id="node7" class="node"><title>l6</title>
<ellipse fill="none" stroke="green" cx="927" cy="-162" rx="27" ry="18"/>
<text text-anchor="middle" x="927" y="-158.3" font-family="Arial" font-size="14.00">6</text>
</g>
<!-- l2&#45;&gt;l6 -->
<g id="edge6" class="edge"><title>l2&#45;&gt;l6</title>
<path fill="none" stroke="green" d="M734.941,-225.241C773.562,-212.725 849.715,-188.046 893.637,-173.812"/>
<polygon fill="green" stroke="green" points="894.847,-177.099 903.281,-170.687 892.689,-170.44 894.847,-177.099"/>
</g>
<!-- l7 -->
<g id="node8" class="node"><title>l7</title>
<ellipse fill="none" stroke="black" cx="99" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="99" y="-86.3" font-family="Arial" font-size="14.00">7</text>
</g>
<!-- l3&#45;&gt;l7 -->
<g id="edge7" class="edge"><title>l3&#45;&gt;l7</title>
<path fill="none" stroke="green" d="M188.188,-148.807C170.998,-137.665 145.382,-121.062 126.007,-108.504"/>
<polygon fill="green" stroke="green" points="127.892,-105.555 117.597,-103.053 124.084,-111.429 127.892,-105.555"/>
</g>
<!-- l8 -->
<g id="node9" class="node"><title>l8</title>
<ellipse fill="none" stroke="black" cx="207" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="207" y="-86.3" font-family="Arial" font-size="14.00">8</text>
</g>
<!-- l3&#45;&gt;l8 -->
<g id="edge8" class="edge"><title>l3&#45;&gt;l8</title>
<path fill="none" stroke="green" d="M207,-143.697C207,-135.983 207,-126.712 207,-118.112"/>
<polygon fill="green" stroke="green" points="210.5,-118.104 207,-108.104 203.5,-118.104 210.5,-118.104"/>
</g>
<!-- l9 -->
<g id="node10" class="node"><title>l9</title>
<ellipse fill="none" stroke="black" cx="387" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="387" y="-86.3" font-family="Arial" font-size="14.00">9</text>
</g>
<!-- l4&#45;&gt;l9 -->
<g id="edge9" class="edge"><title>l4&#45;&gt;l9</title>
<path fill="none" stroke="green" d="M414.65,-144.765C410.288,-136.283 404.853,-125.714 399.959,-116.197"/>
<polygon fill="green" stroke="green" points="402.99,-114.439 395.304,-107.147 396.765,-117.641 402.99,-114.439"/>
</g>
<!-- l10 -->
<g id="node11" class="node"><title>l10</title>
<ellipse fill="none" stroke="black" cx="459" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="459" y="-86.3" font-family="Arial" font-size="14.00">10</text>
</g>
<!-- l4&#45;&gt;l10 -->
<g id="edge10" class="edge"><title>l4&#45;&gt;l10</title>
<path fill="none" stroke="green" d="M431.35,-144.765C435.712,-136.283 441.147,-125.714 446.041,-116.197"/>
<polygon fill="green" stroke="green" points="449.235,-117.641 450.696,-107.147 443.01,-114.439 449.235,-117.641"/>
</g>
<!-- l11 -->
<g id="node12" class="node"><title>l11</title>
<ellipse fill="none" stroke="black" cx="675" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="675" y="-86.3" font-family="Arial" font-size="14.00">11</text>
</g>
<!-- l5&#45;&gt;l11 -->
<g id="edge11" class="edge"><title>l5&#45;&gt;l11</title>
<path fill="none" stroke="green" d="M702.65,-144.765C698.288,-136.283 692.853,-125.714 687.959,-116.197"/>
<polygon fill="green" stroke="green" points="690.99,-114.439 683.304,-107.147 684.765,-117.641 690.99,-114.439"/>
</g>
<!-- l12 -->
<g id="node13" class="node"><title>l12</title>
<ellipse fill="none" stroke="black" cx="747" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="747" y="-86.3" font-family="Arial" font-size="14.00">12</text>
</g>
<!-- l5&#45;&gt;l12 -->
<g id="edge12" class="edge"><title>l5&#45;&gt;l12</title>
<path fill="none" stroke="green" d="M719.35,-144.765C723.712,-136.283 729.147,-125.714 734.041,-116.197"/>
<polygon fill="green" stroke="green" points="737.235,-117.641 738.696,-107.147 731.01,-114.439 737.235,-117.641"/>
</g>
<!-- l13 -->
<g id="node14" class="node"><title>l13</title>
<ellipse fill="none" stroke="black" cx="927" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="927" y="-86.3" font-family="Arial" font-size="14.00">13</text>
</g>
<!-- l6&#45;&gt;l13 -->
<g id="edge13" class="edge"><title>l6&#45;&gt;l13</title>
<path fill="none" stroke="green" d="M927,-143.697C927,-135.983 927,-126.712 927,-118.112"/>
<polygon fill="green" stroke="green" points="930.5,-118.104 927,-108.104 923.5,-118.104 930.5,-118.104"/>
</g>
<!-- l14 -->
<g id="node15" class="node"><title>l14</title>
<ellipse fill="none" stroke="black" cx="1035" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="1035" y="-86.3" font-family="Arial" font-size="14.00">14</text>
</g>
<!-- l6&#45;&gt;l14 -->
<g id="edge14" class="edge"><title>l6&#45;&gt;l14</title>
<path fill="none" stroke="green" d="M945.812,-148.807C963.002,-137.665 988.618,-121.062 1007.99,-108.504"/>
<polygon fill="green" stroke="green" points="1009.92,-111.429 1016.4,-103.053 1006.11,-105.555 1009.92,-111.429"/>
</g>
<!-- l15 -->
<g id="node16" class="node"><title>l15</title>
<ellipse fill="none" stroke="black" cx="27" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-14.3" font-family="Arial" font-size="14.00">15</text>
</g>
<!-- l7&#45;&gt;l15 -->
<g id="edge15" class="edge"><title>l7&#45;&gt;l15</title>
<path fill="none" stroke="yellow" d="M84.4297,-74.8345C74.2501,-64.9376 60.4761,-51.5462 48.9694,-40.3591"/>
<polygon fill="yellow" stroke="yellow" points="51.4055,-37.8461 41.7957,-33.3847 46.5259,-42.865 51.4055,-37.8461"/>
</g>
<!-- l16 -->
<g id="node17" class="node"><title>l16</title>
<ellipse fill="none" stroke="black" cx="99" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="99" y="-14.3" font-family="Arial" font-size="14.00">16</text>
</g>
<!-- l7&#45;&gt;l16 -->
<g id="edge16" class="edge"><title>l7&#45;&gt;l16</title>
<path fill="none" stroke="yellow" d="M99,-71.6966C99,-63.9827 99,-54.7125 99,-46.1124"/>
<polygon fill="yellow" stroke="yellow" points="102.5,-46.1043 99,-36.1043 95.5001,-46.1044 102.5,-46.1043"/>
</g>
<!-- l17 -->
<g id="node18" class="node"><title>l17</title>
<ellipse fill="none" stroke="black" cx="171" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="171" y="-14.3" font-family="Arial" font-size="14.00">17</text>
</g>
<!-- l8&#45;&gt;l17 -->
<g id="edge17" class="edge"><title>l8&#45;&gt;l17</title>
<path fill="none" stroke="yellow" d="M198.65,-72.7646C194.288,-64.2831 188.853,-53.7144 183.959,-44.1974"/>
<polygon fill="yellow" stroke="yellow" points="186.99,-42.4395 179.304,-35.1473 180.765,-45.6409 186.99,-42.4395"/>
</g>
<!-- l18 -->
<g id="node19" class="node"><title>l18</title>
<ellipse fill="none" stroke="black" cx="243" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="243" y="-14.3" font-family="Arial" font-size="14.00">18</text>
</g>
<!-- l8&#45;&gt;l18 -->
<g id="edge18" class="edge"><title>l8&#45;&gt;l18</title>
<path fill="none" stroke="yellow" d="M215.35,-72.7646C219.712,-64.2831 225.147,-53.7144 230.041,-44.1974"/>
<polygon fill="yellow" stroke="yellow" points="233.235,-45.6409 234.696,-35.1473 227.01,-42.4395 233.235,-45.6409"/>
</g>
<!-- l19 -->
<g id="node20" class="node"><title>l19</title>
<ellipse fill="none" stroke="black" cx="315" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="315" y="-14.3" font-family="Arial" font-size="14.00">19</text>
</g>
<!-- l9&#45;&gt;l19 -->
<g id="edge19" class="edge"><title>l9&#45;&gt;l19</title>
<path fill="none" stroke="yellow" d="M372.43,-74.8345C362.25,-64.9376 348.476,-51.5462 336.969,-40.3591"/>
<polygon fill="yellow" stroke="yellow" points="339.405,-37.8461 329.796,-33.3847 334.526,-42.865 339.405,-37.8461"/>
</g>
<!-- l20 -->
<g id="node21" class="node"><title>l20</title>
<ellipse fill="none" stroke="black" cx="387" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="387" y="-14.3" font-family="Arial" font-size="14.00">20</text>
</g>
<!-- l9&#45;&gt;l20 -->
<g id="edge20" class="edge"><title>l9&#45;&gt;l20</title>
<path fill="none" stroke="yellow" d="M387,-71.6966C387,-63.9827 387,-54.7125 387,-46.1124"/>
<polygon fill="yellow" stroke="yellow" points="390.5,-46.1043 387,-36.1043 383.5,-46.1044 390.5,-46.1043"/>
</g>
<!-- l21 -->
<g id="node22" class="node"><title>l21</title>
<ellipse fill="none" stroke="black" cx="459" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="459" y="-14.3" font-family="Arial" font-size="14.00">21</text>
</g>
<!-- l10&#45;&gt;l21 -->
<g id="edge21" class="edge"><title>l10&#45;&gt;l21</title>
<path fill="none" stroke="yellow" d="M459,-71.6966C459,-63.9827 459,-54.7125 459,-46.1124"/>
<polygon fill="yellow" stroke="yellow" points="462.5,-46.1043 459,-36.1043 455.5,-46.1044 462.5,-46.1043"/>
</g>
<!-- l22 -->
<g id="node23" class="node"><title>l22</title>
<ellipse fill="none" stroke="black" cx="531" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="531" y="-14.3" font-family="Arial" font-size="14.00">22</text>
</g>
<!-- l10&#45;&gt;l22 -->
<g id="edge22" class="edge"><title>l10&#45;&gt;l22</title>
<path fill="none" stroke="yellow" d="M473.57,-74.8345C483.75,-64.9376 497.524,-51.5462 509.031,-40.3591"/>
<polygon fill="yellow" stroke="yellow" points="511.474,-42.865 516.204,-33.3847 506.595,-37.8461 511.474,-42.865"/>
</g>
<!-- l23 -->
<g id="node24" class="node"><title>l23</title>
<ellipse fill="none" stroke="black" cx="603" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="603" y="-14.3" font-family="Arial" font-size="14.00">23</text>
</g>
<!-- l11&#45;&gt;l23 -->
<g id="edge23" class="edge"><title>l11&#45;&gt;l23</title>
<path fill="none" stroke="yellow" d="M660.43,-74.8345C650.25,-64.9376 636.476,-51.5462 624.969,-40.3591"/>
<polygon fill="yellow" stroke="yellow" points="627.405,-37.8461 617.796,-33.3847 622.526,-42.865 627.405,-37.8461"/>
</g>
<!-- l24 -->
<g id="node25" class="node"><title>l24</title>
<ellipse fill="none" stroke="black" cx="675" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="675" y="-14.3" font-family="Arial" font-size="14.00">24</text>
</g>
<!-- l11&#45;&gt;l24 -->
<g id="edge24" class="edge"><title>l11&#45;&gt;l24</title>
<path fill="none" stroke="yellow" d="M675,-71.6966C675,-63.9827 675,-54.7125 675,-46.1124"/>
<polygon fill="yellow" stroke="yellow" points="678.5,-46.1043 675,-36.1043 671.5,-46.1044 678.5,-46.1043"/>
</g>
<!-- l25 -->
<g id="node26" class="node"><title>l25</title>
<ellipse fill="none" stroke="black" cx="747" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="747" y="-14.3" font-family="Arial" font-size="14.00">25</text>
</g>
<!-- l12&#45;&gt;l25 -->
<g id="edge25" class="edge"><title>l12&#45;&gt;l25</title>
<path fill="none" stroke="yellow" d="M747,-71.6966C747,-63.9827 747,-54.7125 747,-46.1124"/>
<polygon fill="yellow" stroke="yellow" points="750.5,-46.1043 747,-36.1043 743.5,-46.1044 750.5,-46.1043"/>
</g>
<!-- l26 -->
<g id="node27" class="node"><title>l26</title>
<ellipse fill="none" stroke="black" cx="819" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="819" y="-14.3" font-family="Arial" font-size="14.00">26</text>
</g>
<!-- l12&#45;&gt;l26 -->
<g id="edge26" class="edge"><title>l12&#45;&gt;l26</title>
<path fill="none" stroke="yellow" d="M761.57,-74.8345C771.75,-64.9376 785.524,-51.5462 797.031,-40.3591"/>
<polygon fill="yellow" stroke="yellow" points="799.474,-42.865 804.204,-33.3847 794.595,-37.8461 799.474,-42.865"/>
</g>
<!-- l27 -->
<g id="node28" class="node"><title>l27</title>
<ellipse fill="none" stroke="black" cx="891" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="891" y="-14.3" font-family="Arial" font-size="14.00">27</text>
</g>
<!-- l13&#45;&gt;l27 -->
<g id="edge27" class="edge"><title>l13&#45;&gt;l27</title>
<path fill="none" stroke="yellow" d="M918.65,-72.7646C914.288,-64.2831 908.853,-53.7144 903.959,-44.1974"/>
<polygon fill="yellow" stroke="yellow" points="906.99,-42.4395 899.304,-35.1473 900.765,-45.6409 906.99,-42.4395"/>
</g>
<!-- l28 -->
<g id="node29" class="node"><title>l28</title>
<ellipse fill="none" stroke="black" cx="963" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="963" y="-14.3" font-family="Arial" font-size="14.00">28</text>
</g>
<!-- l13&#45;&gt;l28 -->
<g id="edge28" class="edge"><title>l13&#45;&gt;l28</title>
<path fill="none" stroke="yellow" d="M935.35,-72.7646C939.712,-64.2831 945.147,-53.7144 950.041,-44.1974"/>
<polygon fill="yellow" stroke="yellow" points="953.235,-45.6409 954.696,-35.1473 947.01,-42.4395 953.235,-45.6409"/>
</g>
<!-- l29 -->
<g id="node30" class="node"><title>l29</title>
<ellipse fill="none" stroke="black" cx="1035" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="1035" y="-14.3" font-family="Arial" font-size="14.00">29</text>
</g>
<!-- l14&#45;&gt;l29 -->
<g id="edge29" class="edge"><title>l14&#45;&gt;l29</title>
<path fill="none" stroke="yellow" d="M1035,-71.6966C1035,-63.9827 1035,-54.7125 1035,-46.1124"/>
<polygon fill="yellow" stroke="yellow" points="1038.5,-46.1043 1035,-36.1043 1031.5,-46.1044 1038.5,-46.1043"/>
</g>
<!-- l30 -->
<g id="node31" class="node"><title>l30</title>
<ellipse fill="none" stroke="black" cx="1107" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="1107" y="-14.3" font-family="Arial" font-size="14.00">30</text>
</g>
<!-- l14&#45;&gt;l30 -->
<g id="edge30" class="edge"><title>l14&#45;&gt;l30</title>
<path fill="none" stroke="yellow" d="M1049.57,-74.8345C1059.75,-64.9376 1073.52,-51.5462 1085.03,-40.3591"/>
<polygon fill="yellow" stroke="yellow" points="1087.47,-42.865 1092.2,-33.3847 1082.59,-37.8461 1087.47,-42.865"/>
</g>
</g>
</svg>



Dla drzew binarnych niezbalansowanych ze względu na "luki" należy skok między poziomami rozwiązującymi zmienić na 3 oraz zaczynać tylko i wyłącznie od poziomu korzenia.


//Pokrycie niekompletnego// $BT_{17}$ // przy pomocy dwóch poziomów wierzchołków // 
<svg width="210pt" height="180pt"
 viewBox="0.00 0.00 386.00 332.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 328)">
<title>BST</title>
<polygon fill="white" stroke="none" points="-4,4 -4,-328 382,-328 382,4 -4,4"/>
<!-- l0 -->
<g id="node1" class="node"><title>l0</title>
<ellipse fill="none" stroke="green" cx="207" cy="-306" rx="27" ry="18"/>
<text text-anchor="middle" x="207" y="-302.3" font-family="Arial" font-size="14.00">0</text>
</g>
<!-- l1 -->
<g id="node2" class="node"><title>l1</title>
<ellipse fill="none" stroke="black" cx="171" cy="-234" rx="27" ry="18"/>
<text text-anchor="middle" x="171" y="-230.3" font-family="Arial" font-size="14.00">1</text>
</g>
<!-- l0&#45;&gt;l1 -->
<g id="edge1" class="edge"><title>l0&#45;&gt;l1</title>
<path fill="none" stroke="green" d="M198.65,-288.765C194.288,-280.283 188.853,-269.714 183.959,-260.197"/>
<polygon fill="green" stroke="green" points="186.99,-258.439 179.304,-251.147 180.765,-261.641 186.99,-258.439"/>
</g>
<!-- l2 -->
<g id="node3" class="node"><title>l2</title>
<ellipse fill="none" stroke="black" cx="243" cy="-234" rx="27" ry="18"/>
<text text-anchor="middle" x="243" y="-230.3" font-family="Arial" font-size="14.00">2</text>
</g>
<!-- l0&#45;&gt;l2 -->
<g id="edge2" class="edge"><title>l0&#45;&gt;l2</title>
<path fill="none" stroke="green" d="M215.35,-288.765C219.712,-280.283 225.147,-269.714 230.041,-260.197"/>
<polygon fill="green" stroke="green" points="233.235,-261.641 234.696,-251.147 227.01,-258.439 233.235,-261.641"/>
</g>
<!-- l3 -->
<g id="node4" class="node"><title>l3</title>
<ellipse fill="none" stroke="black" cx="99" cy="-162" rx="27" ry="18"/>
<text text-anchor="middle" x="99" y="-158.3" font-family="Arial" font-size="14.00">3</text>
</g>
<!-- l1&#45;&gt;l3 -->
<g id="edge3" class="edge"><title>l1&#45;&gt;l3</title>
<path fill="none" stroke="yellow" d="M156.43,-218.834C146.25,-208.938 132.476,-195.546 120.969,-184.359"/>
<polygon fill="yellow" stroke="yellow" points="123.405,-181.846 113.796,-177.385 118.526,-186.865 123.405,-181.846"/>
</g>
<!-- l4 -->
<g id="node5" class="node"><title>l4</title>
<ellipse fill="none" stroke="black" cx="171" cy="-162" rx="27" ry="18"/>
<text text-anchor="middle" x="171" y="-158.3" font-family="Arial" font-size="14.00">4</text>
</g>
<!-- l1&#45;&gt;l4 -->
<g id="edge4" class="edge"><title>l1&#45;&gt;l4</title>
<path fill="none" stroke="yellow" d="M171,-215.697C171,-207.983 171,-198.712 171,-190.112"/>
<polygon fill="yellow" stroke="yellow" points="174.5,-190.104 171,-180.104 167.5,-190.104 174.5,-190.104"/>
</g>
<!-- l5 -->
<g id="node6" class="node"><title>l5</title>
<ellipse fill="none" stroke="black" cx="243" cy="-162" rx="27" ry="18"/>
<text text-anchor="middle" x="243" y="-158.3" font-family="Arial" font-size="14.00">5</text>
</g>
<!-- l2&#45;&gt;l5 -->
<g id="edge5" class="edge"><title>l2&#45;&gt;l5</title>
<path fill="none" stroke="yellow" d="M243,-215.697C243,-207.983 243,-198.712 243,-190.112"/>
<polygon fill="yellow" stroke="yellow" points="246.5,-190.104 243,-180.104 239.5,-190.104 246.5,-190.104"/>
</g>
<!-- l6 -->
<g id="node7" class="node"><title>l6</title>
<ellipse fill="none" stroke="black" cx="315" cy="-162" rx="27" ry="18"/>
<text text-anchor="middle" x="315" y="-158.3" font-family="Arial" font-size="14.00">6</text>
</g>
<!-- l2&#45;&gt;l6 -->
<g id="edge6" class="edge"><title>l2&#45;&gt;l6</title>
<path fill="none" stroke="yellow" d="M257.57,-218.834C267.75,-208.938 281.524,-195.546 293.031,-184.359"/>
<polygon fill="yellow" stroke="yellow" points="295.474,-186.865 300.204,-177.385 290.595,-181.846 295.474,-186.865"/>
</g>
<!-- l7 -->
<g id="node8" class="node"><title>l7</title>
<ellipse fill="none" stroke="green" cx="27" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-86.3" font-family="Arial" font-size="14.00">7</text>
</g>
<!-- l3&#45;&gt;l7 -->
<g id="edge7" class="edge"><title>l3&#45;&gt;l7</title>
<path fill="none" stroke="green" d="M84.4297,-146.834C74.2501,-136.938 60.4761,-123.546 48.9694,-112.359"/>
<polygon fill="green" stroke="green" points="51.4055,-109.846 41.7957,-105.385 46.5259,-114.865 51.4055,-109.846"/>
</g>
<!-- l8 -->
<g id="node9" class="node"><title>l8</title>
<ellipse fill="none" stroke="green" cx="99" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="99" y="-86.3" font-family="Arial" font-size="14.00">8</text>
</g>
<!-- l3&#45;&gt;l8 -->
<g id="edge8" class="edge"><title>l3&#45;&gt;l8</title>
<path fill="none" stroke="green" d="M99,-143.697C99,-135.983 99,-126.712 99,-118.112"/>
<polygon fill="green" stroke="green" points="102.5,-118.104 99,-108.104 95.5001,-118.104 102.5,-118.104"/>
</g>
<!-- l9 -->
<g id="node10" class="node"><title>l9</title>
<ellipse fill="none" stroke="green" cx="171" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="171" y="-86.3" font-family="Arial" font-size="14.00">9</text>
</g>
<!-- l4&#45;&gt;l9 -->
<g id="edge9" class="edge"><title>l4&#45;&gt;l9</title>
<path fill="none" stroke="green" d="M171,-143.697C171,-135.983 171,-126.712 171,-118.112"/>
<polygon fill="green" stroke="green" points="174.5,-118.104 171,-108.104 167.5,-118.104 174.5,-118.104"/>
</g>
<!-- l13 -->
<g id="node11" class="node"><title>l13</title>
<ellipse fill="none" stroke="green" cx="279" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="279" y="-86.3" font-family="Arial" font-size="14.00">13</text>
</g>
<!-- l6&#45;&gt;l13 -->
<g id="edge10" class="edge"><title>l6&#45;&gt;l13</title>
<path fill="none" stroke="green" d="M306.65,-144.765C302.288,-136.283 296.853,-125.714 291.959,-116.197"/>
<polygon fill="green" stroke="green" points="294.99,-114.439 287.304,-107.147 288.765,-117.641 294.99,-114.439"/>
</g>
<!-- l14 -->
<g id="node12" class="node"><title>l14</title>
<ellipse fill="none" stroke="green" cx="351" cy="-90" rx="27" ry="18"/>
<text text-anchor="middle" x="351" y="-86.3" font-family="Arial" font-size="14.00">14</text>
</g>
<!-- l6&#45;&gt;l14 -->
<g id="edge11" class="edge"><title>l6&#45;&gt;l14</title>
<path fill="none" stroke="green" d="M323.35,-144.765C327.712,-136.283 333.147,-125.714 338.041,-116.197"/>
<polygon fill="green" stroke="green" points="341.235,-117.641 342.696,-107.147 335.01,-114.439 341.235,-117.641"/>
</g>
<!-- l17 -->
<g id="node13" class="node"><title>l17</title>
<ellipse fill="none" stroke="black" cx="27" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-14.3" font-family="Arial" font-size="14.00">17</text>
</g>
<!-- l8&#45;&gt;l17 -->
<g id="edge12" class="edge"><title>l8&#45;&gt;l17</title>
<path fill="none" stroke="green" d="M84.4297,-74.8345C74.2501,-64.9376 60.4761,-51.5462 48.9694,-40.3591"/>
<polygon fill="green" stroke="green" points="51.4055,-37.8461 41.7957,-33.3847 46.5259,-42.865 51.4055,-37.8461"/>
</g>
<!-- l18 -->
<g id="node14" class="node"><title>l18</title>
<ellipse fill="none" stroke="black" cx="99" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="99" y="-14.3" font-family="Arial" font-size="14.00">18</text>
</g>
<!-- l8&#45;&gt;l18 -->
<g id="edge13" class="edge"><title>l8&#45;&gt;l18</title>
<path fill="none" stroke="green" d="M99,-71.6966C99,-63.9827 99,-54.7125 99,-46.1124"/>
<polygon fill="green" stroke="green" points="102.5,-46.1043 99,-36.1043 95.5001,-46.1044 102.5,-46.1043"/>
</g>
<!-- l19 -->
<g id="node15" class="node"><title>l19</title>
<ellipse fill="none" stroke="black" cx="171" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="171" y="-14.3" font-family="Arial" font-size="14.00">19</text>
</g>
<!-- l9&#45;&gt;l19 -->
<g id="edge14" class="edge"><title>l9&#45;&gt;l19</title>
<path fill="none" stroke="green" d="M171,-71.6966C171,-63.9827 171,-54.7125 171,-46.1124"/>
<polygon fill="green" stroke="green" points="174.5,-46.1043 171,-36.1043 167.5,-46.1044 174.5,-46.1043"/>
</g>
<!-- l27 -->
<g id="node16" class="node"><title>l27</title>
<ellipse fill="none" stroke="black" cx="279" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="279" y="-14.3" font-family="Arial" font-size="14.00">27</text>
</g>
<!-- l13&#45;&gt;l27 -->
<g id="edge15" class="edge"><title>l13&#45;&gt;l27</title>
<path fill="none" stroke="green" d="M279,-71.6966C279,-63.9827 279,-54.7125 279,-46.1124"/>
<polygon fill="green" stroke="green" points="282.5,-46.1043 279,-36.1043 275.5,-46.1044 282.5,-46.1043"/>
</g>
<!-- l30 -->
<g id="node17" class="node"><title>l30</title>
<ellipse fill="none" stroke="black" cx="351" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="351" y="-14.3" font-family="Arial" font-size="14.00">30</text>
</g>
<!-- l14&#45;&gt;l30 -->
<g id="edge16" class="edge"><title>l14&#45;&gt;l30</title>
<path fill="none" stroke="green" d="M351,-71.6966C351,-63.9827 351,-54.7125 351,-46.1124"/>
<polygon fill="green" stroke="green" points="354.5,-46.1043 351,-36.1043 347.5,-46.1044 354.5,-46.1043"/>
</g>
</g>
</svg>


===== Cykle =====

Grafy $C_n$ (o parzystej i nieparzystej długości) są optymalnie pokryte po przez $\lceil n/5 \rceil$ wierzchołków. Dowolna para takiego cyklu go pokrywa, pod warunkiem, że między wierzchołkami jest odległość $<n \mod 5;5>$ dla $n \mod 5 \ne 0$. Dla $n \mod 5 = 0$ odległość zawsze wynosi 5.  

//Pokrycie // $C_7$ // przy pomocy dwóch wierzchołków//
<svg width="219pt" height="212pt"
 viewBox="0.00 0.00 328.85 317.71" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 313.71)">
<title>%3</title>
<polygon fill="white" stroke="none" points="-4,4 -4,-313.71 324.848,-313.71 324.848,4 -4,4"/>
<!-- 0 -->
<g id="node1" class="node"><title>0</title>
<ellipse fill="none" stroke="green" cx="240.995" cy="-45.1058" rx="27" ry="18"/>
<text text-anchor="middle" x="240.995" y="-41.4058" font-family="Times New Roman,serif" font-size="14.00">0</text>
</g>
<!-- 1 -->
<g id="node2" class="node"><title>1</title>
<ellipse fill="none" stroke="black" cx="122.237" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="122.237" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">1</text>
</g>
<!-- 0&#45;&#45;1 -->
<g id="edge1" class="edge"><title>0&#45;&#45;1</title>
<path fill="none" stroke="green" d="M215.227,-39.2243C195.307,-34.6777 167.863,-28.4138 147.955,-23.8701"/>
</g>
<!-- 6 -->
<g id="node7" class="node"><title>6</title>
<ellipse fill="none" stroke="black" cx="293.848" cy="-154.855" rx="27" ry="18"/>
<text text-anchor="middle" x="293.848" y="-151.155" font-family="Times New Roman,serif" font-size="14.00">6</text>
</g>
<!-- 0&#45;&#45;6 -->
<g id="edge2" class="edge"><title>0&#45;&#45;6</title>
<path fill="none" stroke="green" d="M249.254,-62.2542C259.125,-82.7518 275.551,-116.861 285.473,-137.465"/>
</g>
<!-- 2 -->
<g id="node3" class="node"><title>2</title>
<ellipse fill="none" stroke="green" cx="27" cy="-93.9489" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-90.2489" font-family="Times New Roman,serif" font-size="14.00">2</text>
</g>
<!-- 1&#45;&#45;2 -->
<g id="edge3" class="edge"><title>1&#45;&#45;2</title>
<path fill="none" stroke="green" d="M104.769,-31.9302C87.5852,-45.6338 61.5026,-66.434 44.3572,-80.107"/>
</g>
<!-- 3 -->
<g id="node4" class="node"><title>3</title>
<ellipse fill="none" stroke="black" cx="27" cy="-215.761" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-212.061" font-family="Times New Roman,serif" font-size="14.00">3</text>
</g>
<!-- 2&#45;&#45;3 -->
<g id="edge4" class="edge"><title>2&#45;&#45;3</title>
<path fill="none" stroke="green" d="M27,-112.185C27,-135.15 27,-174.377 27,-197.4"/>
</g>
<!-- 4 -->
<g id="node5" class="node"><title>4</title>
<ellipse fill="none" stroke="black" cx="122.237" cy="-291.71" rx="27" ry="18"/>
<text text-anchor="middle" x="122.237" y="-288.01" font-family="Times New Roman,serif" font-size="14.00">4</text>
</g>
<!-- 3&#45;&#45;4 -->
<g id="edge5" class="edge"><title>3&#45;&#45;4</title>
<path fill="none" stroke="yellow" d="M44.4679,-229.692C61.6517,-243.395 87.7343,-264.195 104.88,-277.868"/>
</g>
<!-- 5 -->
<g id="node6" class="node"><title>5</title>
<ellipse fill="none" stroke="black" cx="240.995" cy="-264.605" rx="27" ry="18"/>
<text text-anchor="middle" x="240.995" y="-260.905" font-family="Times New Roman,serif" font-size="14.00">5</text>
</g>
<!-- 4&#45;&#45;5 -->
<g id="edge6" class="edge"><title>4&#45;&#45;5</title>
<path fill="none" stroke="black" d="M148.006,-285.829C167.925,-281.282 195.37,-275.018 215.277,-270.475"/>
</g>
<!-- 5&#45;&#45;6 -->
<g id="edge7" class="edge"><title>5&#45;&#45;6</title>
<path fill="none" stroke="yellow" d="M249.254,-247.456C259.125,-226.959 275.551,-192.849 285.473,-172.245"/>
</g>
</g>
</svg>


===== Wnioski =====

Problem $VC^{(k)}$  gdzie $k \ge 3$ jest dalszym rozwinięciem problemu $VC^{(2)}$. Algorytmy Weryfikacji Pokrycia Grafu przez rozwiązanie, Zachłanny, Pełenego Przeglądu Grafu oraz Przybliżony dla wyższych problemów $VC^{(k)}$ mają $n^{k-2}$ razy większą złożoność( w Algorytmie Weryfikacji pojawia się dodatkowych $k-2$ pętli). 

Najlepsze rozwiązanie za każdym razem zwróci tylko algorytm Pełnego Przeglądu Grafu. Algorytm zachłanny w przypadku, gdy istnieje kilka wierzchołków, które pokrywają taką samą liczbę niepokrytych wierzchołków mogą wybrać taki wierzchołek, który spowoduje w przyszłości rozdzielenie niepokrytych wierzchołków na osobne podgrafy, a w konsekwencji użycia większej ilości wierzchołków, niż posiadałoby najlepsze rozwiązanie. Rozwiązanie przybliżone ma natomiast niewielką szansę na zwrócenie najlepszego rozwiązania, za to jednak otrzymujemy rozwiązanie dobre w dużo krótszym czasie.


===== Literatura =====

  *[[https://www.youtube.com/watch?v=ZZxj9hqldng]] Vertex cover Problem with example
  *[[https://www.youtube.com/watch?v=m_dOtat56vY]] Vertex Cover - Georgia Tech - Computability, Complexity, Theory: Algorithms
  *[[https://www.youtube.com/watch?v=_8wrCTLwC7E]] Vertex Cover Solution - Intro to Theoretical Computer Science

----
====== Ilustracja Problemu ======

===== Legenda =====

^ Wierzchołki ^^ Krawędzie^^
^ Oznaczenie ^ Znaczenie ^ Oznaczenie ^ Znaczenie ^
| "zielony" | Wierzchołek należący do grupy odpowiedzi | "zielony" | Krawędź łącząca bezpośrednio zielony wierzchołek z pierwszym sąsiadem|
| --- | --- | "żółty | Krawędź łącząca pośrednio zielony wierzchołek z drugim sąsiadem|
| "czarny" | Zwykły wierzchołek nie należący zarówno do grupy odpowiedzi jak i grupy niepokrytych wierzchołków | "czarny" | Zwykła krawędź ( nie pokrywa grafu ) |
| "czerwony" | Niepokryty wierzchołek | --- | --- |

===== Prawidłowe Pokrycie =====

<svg width="383pt" height="365pt"
 viewBox="0.00 0.00 382.86 364.86" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 360.856)">
<title>%3</title>
<polygon fill="white" stroke="none" points="-4,4 -4,-360.856 378.856,-360.856 378.856,4 -4,4"/>
<!-- 0 -->
<g id="node1" class="node"><title>0</title>
<ellipse fill="none" stroke="black" cx="187.428" cy="-338.856" rx="27" ry="18"/>
<text text-anchor="middle" x="187.428" y="-335.156" font-family="Times New Roman,serif" font-size="14.00">0</text>
</g>
<!-- 1 -->
<g id="node2" class="node"><title>1</title>
<ellipse fill="none" stroke="black" cx="347.856" cy="-178.428" rx="27" ry="18"/>
<text text-anchor="middle" x="347.856" y="-174.728" font-family="Times New Roman,serif" font-size="14.00">1</text>
</g>
<!-- 0&#45;&#45;1 -->
<g id="edge1" class="edge"><title>0&#45;&#45;1</title>
<path fill="none" stroke="yellow" d="M202.521,-323.764C233.097,-293.187 302.047,-224.238 332.687,-193.598"/>
</g>
<!-- 2 -->
<g id="node3" class="node"><title>2</title>
<ellipse fill="none" stroke="green" cx="73.9883" cy="-64.9883" rx="27" ry="18"/>
<text text-anchor="middle" x="73.9883" y="-61.2883" font-family="Times New Roman,serif" font-size="14.00">2</text>
</g>
<!-- 0&#45;&#45;2 -->
<g id="edge2" class="edge"><title>0&#45;&#45;2</title>
<path fill="none" stroke="green" d="M180.159,-321.308C159.67,-271.842 101.612,-131.678 81.1965,-82.3905"/>
</g>
<!-- 3 -->
<g id="node4" class="node"><title>3</title>
<ellipse fill="none" stroke="black" cx="73.9883" cy="-291.868" rx="27" ry="18"/>
<text text-anchor="middle" x="73.9883" y="-288.168" font-family="Times New Roman,serif" font-size="14.00">3</text>
</g>
<!-- 0&#45;&#45;3 -->
<g id="edge3" class="edge"><title>0&#45;&#45;3</title>
<path fill="none" stroke="yellow" d="M164.472,-329.348C144.92,-321.249 116.953,-309.664 97.2998,-301.524"/>
</g>
<!-- 4 -->
<g id="node5" class="node"><title>4</title>
<ellipse fill="none" stroke="black" cx="300.868" cy="-291.868" rx="27" ry="18"/>
<text text-anchor="middle" x="300.868" y="-288.168" font-family="Times New Roman,serif" font-size="14.00">4</text>
</g>
<!-- 0&#45;&#45;4 -->
<g id="edge4" class="edge"><title>0&#45;&#45;4</title>
<path fill="none" stroke="yellow" d="M210.384,-329.348C229.936,-321.249 257.904,-309.664 277.557,-301.524"/>
</g>
<!-- 7 -->
<g id="node8" class="node"><title>7</title>
<ellipse fill="none" stroke="black" cx="300.868" cy="-64.9883" rx="27" ry="18"/>
<text text-anchor="middle" x="300.868" y="-61.2883" font-family="Times New Roman,serif" font-size="14.00">7</text>
</g>
<!-- 0&#45;&#45;7 -->
<g id="edge5" class="edge"><title>0&#45;&#45;7</title>
<path fill="none" stroke="yellow" d="M194.697,-321.308C215.186,-271.842 273.244,-131.678 293.66,-82.3905"/>
</g>
<!-- 1&#45;&#45;2 -->
<g id="edge6" class="edge"><title>1&#45;&#45;2</title>
<path fill="none" stroke="green" d="M324.507,-168.756C272.765,-147.324 148.966,-96.0449 97.2791,-74.6357"/>
</g>
<!-- 1&#45;&#45;3 -->
<g id="edge7" class="edge"><title>1&#45;&#45;3</title>
<path fill="none" stroke="yellow" d="M324.507,-188.1C272.765,-209.532 148.966,-260.811 97.2791,-282.221"/>
</g>
<!-- 1&#45;&#45;4 -->
<g id="edge8" class="edge"><title>1&#45;&#45;4</title>
<path fill="none" stroke="yellow" d="M340.514,-196.153C331.687,-217.465 316.963,-253.012 308.158,-274.268"/>
</g>
<!-- 2&#45;&#45;4 -->
<g id="edge9" class="edge"><title>2&#45;&#45;4</title>
<path fill="none" stroke="green" d="M89.2268,-80.2268C130.558,-121.558 244.442,-235.442 285.696,-276.696"/>
</g>
<!-- 5 -->
<g id="node6" class="node"><title>5</title>
<ellipse fill="none" stroke="black" cx="27" cy="-178.428" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-174.728" font-family="Times New Roman,serif" font-size="14.00">5</text>
</g>
<!-- 2&#45;&#45;5 -->
<g id="edge10" class="edge"><title>2&#45;&#45;5</title>
<path fill="none" stroke="green" d="M66.6464,-82.7133C57.8189,-104.025 43.0949,-139.572 34.2904,-160.828"/>
</g>
<!-- 6 -->
<g id="node7" class="node"><title>6</title>
<ellipse fill="none" stroke="green" cx="187.428" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="187.428" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">6</text>
</g>
<!-- 2&#45;&#45;6 -->
<g id="edge11" class="edge"><title>2&#45;&#45;6</title>
<path fill="none" stroke="green" d="M96.9446,-55.4795C116.496,-47.3809 144.464,-35.7964 164.117,-27.6559"/>
</g>
<!-- 2&#45;&#45;7 -->
<g id="edge12" class="edge"><title>2&#45;&#45;7</title>
<path fill="none" stroke="green" d="M101.355,-64.9883C145.08,-64.9883 230.194,-64.9883 273.757,-64.9883"/>
</g>
<!-- 3&#45;&#45;4 -->
<g id="edge13" class="edge"><title>3&#45;&#45;4</title>
<path fill="none" stroke="yellow" d="M101.355,-291.868C145.08,-291.868 230.194,-291.868 273.757,-291.868"/>
</g>
<!-- 3&#45;&#45;5 -->
<g id="edge14" class="edge"><title>3&#45;&#45;5</title>
<path fill="none" stroke="yellow" d="M66.6464,-274.143C57.8189,-252.832 43.0949,-217.285 34.2904,-196.029"/>
</g>
<!-- 3&#45;&#45;6 -->
<g id="edge15" class="edge"><title>3&#45;&#45;6</title>
<path fill="none" stroke="green" d="M81.2571,-274.32C101.747,-224.854 159.805,-84.6892 180.22,-35.4021"/>
</g>
<!-- 3&#45;&#45;7 -->
<g id="edge16" class="edge"><title>3&#45;&#45;7</title>
<path fill="none" stroke="yellow" d="M89.2268,-276.63C130.558,-235.298 244.442,-121.414 285.696,-80.1605"/>
</g>
<!-- 6&#45;&#45;7 -->
<g id="edge17" class="edge"><title>6&#45;&#45;7</title>
<path fill="none" stroke="green" d="M210.384,-27.5088C229.936,-35.6074 257.904,-47.1919 277.557,-55.3324"/>
</g>
</g>
</svg>

** Macierz **
<code python>
[0, 1, 1, 1, 1, 0, 0, 1]
[1, 0, 1, 1, 1, 0, 0, 0]
[1, 1, 0, 0, 1, 1, 1, 1]
[1, 1, 0, 0, 1, 1, 1, 1]
[1, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 1]
[1, 0, 1, 1, 0, 0, 1, 0]
</code>

** Wierzchołki należące do zbioru rozwiązania **

<code python>
[2,6]
</code>

===== Niepowodzenie =====

<svg width="428pt" height="318pt"
 viewBox="0.00 0.00 427.85 317.71" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 313.71)">
<title>%3</title>
<polygon fill="white" stroke="none" points="-4,4 -4,-313.71 423.848,-313.71 423.848,4 -4,4"/>
<!-- 0 -->
<g id="node1" class="node"><title>0</title>
<ellipse fill="none" stroke="green" cx="240.995" cy="-45.1058" rx="27" ry="18"/>
<text text-anchor="middle" x="240.995" y="-41.4058" font-family="Times New Roman,serif" font-size="14.00">0</text>
</g>
<!-- 6 -->
<g id="node7" class="node"><title>6</title>
<ellipse fill="none" stroke="black" cx="122.237" cy="-18" rx="27" ry="18"/>
<text text-anchor="middle" x="122.237" y="-14.3" font-family="Times New Roman,serif" font-size="14.00">6</text>
</g>
<!-- 0&#45;&#45;6 -->
<g id="edge1" class="edge"><title>0&#45;&#45;6</title>
<path fill="none" stroke="green" d="M215.227,-39.2243C195.307,-34.6777 167.863,-28.4138 147.955,-23.8701"/>
</g>
<!-- 7 -->
<g id="node8" class="node"><title>7</title>
<ellipse fill="none" stroke="black" cx="240.995" cy="-264.605" rx="27" ry="18"/>
<text text-anchor="middle" x="240.995" y="-260.905" font-family="Times New Roman,serif" font-size="14.00">7</text>
</g>
<!-- 0&#45;&#45;7 -->
<g id="edge2" class="edge"><title>0&#45;&#45;7</title>
<path fill="none" stroke="green" d="M240.995,-63.4426C240.995,-104.863 240.995,-205.251 240.995,-246.474"/>
</g>
<!-- 1 -->
<g id="node2" class="node"><title>1</title>
<ellipse fill="none" stroke="green" cx="27" cy="-93.9489" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-90.2489" font-family="Times New Roman,serif" font-size="14.00">1</text>
</g>
<!-- 4 -->
<g id="node5" class="node"><title>4</title>
<ellipse fill="none" stroke="black" cx="27" cy="-215.761" rx="27" ry="18"/>
<text text-anchor="middle" x="27" y="-212.061" font-family="Times New Roman,serif" font-size="14.00">4</text>
</g>
<!-- 1&#45;&#45;4 -->
<g id="edge3" class="edge"><title>1&#45;&#45;4</title>
<path fill="none" stroke="green" d="M27,-112.185C27,-135.15 27,-174.377 27,-197.4"/>
</g>
<!-- 1&#45;&#45;6 -->
<g id="edge4" class="edge"><title>1&#45;&#45;6</title>
<path fill="none" stroke="green" d="M44.4679,-80.0187C61.6517,-66.3151 87.7343,-45.5149 104.88,-31.8419"/>
</g>
<!-- 2 -->
<g id="node3" class="node"><title>2</title>
<ellipse fill="none" stroke="black" cx="122.237" cy="-291.71" rx="27" ry="18"/>
<text text-anchor="middle" x="122.237" y="-288.01" font-family="Times New Roman,serif" font-size="14.00">2</text>
</g>
<!-- 2&#45;&#45;4 -->
<g id="edge5" class="edge"><title>2&#45;&#45;4</title>
<path fill="none" stroke="yellow" d="M104.769,-277.78C87.5852,-264.077 61.5026,-243.276 44.3572,-229.603"/>
</g>
<!-- 2&#45;&#45;7 -->
<g id="edge6" class="edge"><title>2&#45;&#45;7</title>
<path fill="none" stroke="yellow" d="M148.006,-285.829C167.925,-281.282 195.37,-275.018 215.277,-270.475"/>
</g>
<!-- 3 -->
<g id="node4" class="node"><title>3</title>
<ellipse fill="none" stroke="black" cx="293.848" cy="-154.855" rx="27" ry="18"/>
<text text-anchor="middle" x="293.848" y="-151.155" font-family="Times New Roman,serif" font-size="14.00">3</text>
</g>
<!-- 3&#45;&#45;4 -->
<g id="edge7" class="edge"><title>3&#45;&#45;4</title>
<path fill="none" stroke="yellow" d="M268.261,-160.695C217.386,-172.307 104.033,-198.179 52.9011,-209.85"/>
</g>
<!-- 5 -->
<g id="node6" class="node"><title>5</title>
<ellipse fill="none" stroke="red" cx="392.848" cy="-154.855" rx="27" ry="18"/>
<text text-anchor="middle" x="392.848" y="-151.155" font-family="Times New Roman,serif" font-size="14.00">5</text>
</g>
<!-- 3&#45;&#45;5 -->
<g id="edge8" class="edge"><title>3&#45;&#45;5</title>
<path fill="none" stroke="black" d="M320.9,-154.855C334.869,-154.855 351.864,-154.855 365.828,-154.855"/>
</g>
<!-- 3&#45;&#45;7 -->
<g id="edge9" class="edge"><title>3&#45;&#45;7</title>
<path fill="none" stroke="yellow" d="M285.59,-172.004C275.719,-192.501 259.292,-226.61 249.37,-247.214"/>
</g>
<!-- 4&#45;&#45;6 -->
<g id="edge10" class="edge"><title>4&#45;&#45;6</title>
<path fill="none" stroke="yellow" d="M35.285,-198.557C53.2965,-161.156 95.8476,-72.7979 113.903,-35.3051"/>
</g>
<!-- 4&#45;&#45;7 -->
<g id="edge11" class="edge"><title>4&#45;&#45;7</title>
<path fill="none" stroke="yellow" d="M52.8128,-221.653C94.0549,-231.066 174.335,-249.39 215.424,-258.768"/>
</g>
<!-- 6&#45;&#45;7 -->
<g id="edge12" class="edge"><title>6&#45;&#45;7</title>
<path fill="none" stroke="yellow" d="M130.588,-35.3407C152.393,-80.6194 210.859,-202.026 232.654,-247.283"/>
</g>
</g>
</svg>

** Macierz **
<code python>
[0, 0, 0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 1, 0, 1, 0]
[0, 0, 0, 0, 1, 0, 0, 1]
[0, 0, 0, 0, 1, 1, 0, 1]
[0, 1, 1, 1, 0, 0, 1, 1]
[0, 0, 0, 1, 0, 0, 0, 0]
[1, 1, 0, 0, 1, 0, 0, 1]
[1, 0, 1, 1, 1, 0, 1, 0]
</code>

** Wierzchołki należące do zbioru rozwiązania **

<code python>
[0,1]
</code>



====== Bez Wizualizacji ======



===== Generowanie grafów ===== 

** Źródło: ** [[https://pw20we.cs.put.poznan.pl/doku.php?id=ok:modele_grafow_losowych]]
<code python>
def gnp(n, p):
    "Model G(n,p)"
    a = [[0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if (random.random() <= p):
                a[i][j] = a[j][i] = 1
    return a
</code>


===== Weryfikacja poprawności rozwiązania =====

^ Dane ^ Opis ^
| ''vertexAmount'' | liczba wierzchołków w grafie |
| ''matrix''  | macierz sąsiedztwa|
| ''answers'' | rozwiązanie poddawane weryfikacji|
| ''check_table'' | tablica z 0 i 1 informująca czy wierzchołek(indeks) został pokryty(1), czy nie(0)|

<code python>
def graph_cover_test(vertexAmount,matrix,answers):
    check_table=[]
    for i in range(vertexAmount):
        check_table.append(0)
    for answer in answers:
        check_table[answer] = 1
        for i in range(vertexAmount):
            if matrix[answer][i] == 1:
                check_table[i]=1
                for j in range(vertexAmount):
                    if matrix[i][j] == 1:
                        check_table[j]=1
    if 0 in check_table:
        return False
    else:
        return True
</code>


** Średnia złożoność: ** 

**$\mathcal{O}(k \cdot n^2)$** 


** Złożoność pesymistyczna: ** 

**$\mathcal{O}(n^3)$**
gdyż w pesymistycznym przypadku **$k$** wynosi **$n$**

| ''k''  | ''liczba wierzchołków w rozwiązaniu''|
| ''n'' | ''liczba wszystkich wierzchołków''|



===== Algorytm zachłanny =====
Algorytm:
  - oblicza ile wierzchołków może pokryć każdy z wierzchołków
  - wybiera najlepszy z nich i dodaje do rozwiązania
  - wykonywany jest test pokrycia grafu - w przypadku powodzenia algorytm kończy pracę, w przeciwnym przypadku usuwa krawędzie wybranego wierzchołka i ponownie wykonuje wszystkie kroki algorytmu

==== Zmodyfikowany algorytm testu pokrycia ====
Do tego algorytmu musimy zmodyfikować algorytm testu pokrycia, tak, aby zwracał oprócz odpowiedzi również liczbę niepokrytych wierzchołków

^ Dane ^ Opis ^
| ''vertexAmount'' | liczba wierzchołków w grafie |
| ''matrix''  | macierz sąsiedztwa|
| ''answers'' | rozwiązanie poddawane weryfikacji|
| ''check_table'' | tablica z 0 i 1 informująca czy wierzchołek(indeks) został pokryty(1), czy nie(0)|
| ''not_covered'' | ''tablica z niepokrytymi wierzchołkami'' |
| ''corectly_covered'' | ''zmienna boolowska, informująca czy "answers" poprawanie pokrywa graf'' |

<code python>
def graph_cover_test_greedy(vertexAmount,matrix,answers):
    check_table=[]
    for i in range(vertexAmount):
        check_table.append(0)
    for answer in answers:
        check_table[answer] = 1
        for i in range(vertexAmount):
            if matrix[answer][i] == 1:
                check_table[i]=1
                for j in range(vertexAmount):
                    if j!=answer:
                        if matrix[i][j] == 1:
                            check_table[j]=1
    not_covered = []
    for e in range(vertexAmount):
        if check_table[e] != 1:
            not_covered.append(e)
    if len(not_covered) > 0:
        corectly_covered = False
    else:
        corectly_covered = True

    return corectly_covered,not_covered
</code>
==== Pomocniczy algorytm zliczający moc pokrycia każdego z wierzchołków ====
^ Dane ^ Opis ^
| ''matrix'' | ''macierz sąsiedztwa'' |
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''covered'' | ''tablica z 0 i 1 informująca czy wierzchołek(indeks) został pokryty(1), czy nie(0)'' |
| ''vertices'' | ''słownik numerów wierzchołków i ilością wierzchołów, które mogą one pokryć'' |
| ''check_table'' | ''tablica z 0 i 1 informująca czy w danym przejściu pętli wierzchołek(indeks) został policzony jako możliwy do pokrycia(1), czy też nie(0)'' |

<code python>
def Connection_counter(matrix,vertexAmount,covered):
    vertices={}
    for vertex in range(vertexAmount):
        vertices[vertex] = 0

    for i in range(vertexAmount):
        check_table = [0 for _ in range(vertexAmount)]
        check_table[i] = 1
        for j in range(vertexAmount):
            if matrix[i][j]==1:
                if check_table[j] == 0:
                    if covered[j] == 0:
                        vertices[i]+=1
                    check_table[j] = 1
                for m in range(vertexAmount):
                    if matrix[j][m] == 1:
                        if check_table[m] == 0:
                            if covered[m] == 0:
                                vertices[i]+=1
                            check_table[m] = 1

    return vertices
</code>


** Złożoność: ** 

**$\mathcal{O}(n^3)$**,
| ''n'' | ''liczba wszystkich wierzchołków''|
==== Właściwy algorytm zachłanny ====
^ Dane ^ Opis ^
| ''matrix''  | ''macierz sąsiedztwa''|
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''matrix_copy'' | ''kopia właściwej macierzy, na której są przeprowadzane działania usuwania polączeń'' |
| ''covered'' | ''tablica z 0 i 1 informująca czy wierzchołek(indeks) został pokryty(1), czy nie(0)'' |
| ''vertices'' | ''słownik numerów wierzchołków i ilością wierzchołów, które mogą one pokryć'' |
| ''solution'' | ''tablica wierzchołków, które pokrywają cały graf'' |
| ''test_result'' | ''zmienna boolowska, informuje czy "solution" pokryło graf i można zakończyć algorytm(True), czy nie(False)'' |
| ''ordered_vertices'' | ''posortowane wierzchołki - od najwięcej niepokrytych wierzchołków pokrywającego do najmniej '' | 
| ''best_one'' | ''wierzchołek, który w danej sytuacji pokrywa najwięcej niepokrytych wierzchołków'' |
| ''not_covered'' | ''tablica zawierająca wierzchołki, których "solution" nie pokrywa'' |

<code python>
import copy

def Greedy_graph_cover_test(matrix,vertexAmount):
    matrix_copy=copy.deepcopy(matrix)

    covered = [0 for _ in range(vertexAmount)]

    vertices = Connection_counter(matrix,vertexAmount,covered)

    solution = []
    test_result = False

    while not test_result:
        ordered_vertices = sorted(vertices, key=vertices.get, reverse=True)
        best_one = ordered_vertices[0]
        while vertices[best_one] == 0 and covered[best_one] == 1:
            vertices.pop(best_one)
            best_one = ordered_vertices[0]
        solution.append(best_one)

        for i in range(vertexAmount):
            if matrix_copy[best_one][i]==1:
                matrix_copy[best_one][i] = 0
                matrix_copy[i][best_one] = 0
                for j in range(vertexAmount):
                    if matrix_copy[i][j] == 1:
                        matrix_copy[i][j] = 0
                        matrix_copy[j][i] = 0

        test_result,not_covered = graph_cover_test_greedy(vertexAmount,matrix,solution)

        covered = [1 for _ in range(vertexAmount)]

        for vertex in not_covered:
            covered[vertex] = 0

        vertices = Connection_counter(matrix_copy, vertexAmount,covered)

    return solution
</code>

** Średnia złożoność: ** 

**$\mathcal{O}(n^3)$** → zazwyczaj pętla while wykona się zaledwie parę razy, a najwięcej czasu zabiera ''Connection_counter''

** Złożoność pesymistyczna: **  
 **$\mathcal{O}(n^4)$**  →  pętla while wykona się ''n'' razy, a razem z nią ''Connection_counter''

| ''n'' | ''liczba wszystkich wierzchołków''|
===== Algorytm przeszukujący wszystkie podzbiory (Brute Force) =====
Algorytm przeszukuje wszystkie podzbiory grafu, wyświetla podzbiory i wynik testu na pokrycie oraz zwraca wszystkie optymalne rozwiązania

==== Algorytm tworzący zbiór potęgowy grafu(Opcjonalnie) ====
Algorytm ten można spokojnie zastąpić funkcją **combinations(table_with_elements,number_of_element_to_choose)** z bibilotek **itertools**

^ Dane ^ Opis ^
| ''tab'' | ''lista z wierzchołkami'' |
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''results''  | ''lista ze wszystkimi podzbiorami grafu''|


<code python>
import copy
#1. Tworzymy tablice wynikowa, z jednym zbiorem pustym
#2. Przechodzimy po elementach tablicy wejsciowej
#3. Dla kazdego zbioru z tablicy wynikowej tworzymy kopie
#4. Nastepnie dodajemy do niej element z tablicy wejsciowej
#4. Nowo powstale zbior dodajemy do puli zbiorow w tablicy wynikowej
#5. Kroki te powtarzamy, az nie skoncza nam sie elementy tablicy wejsciowej

def power_set(tab,vertexAmount):
    results = [[]]                           #przygotowanie tablicy na wyniki
    tmp = []                                #tablica tworzaca kolejne zbior
    # dla kazdego elementu zbioru wejsciowego
    # przechodzimy elementy tablicy z wynikami
    for i in range(vertexAmount):
        for el in results:
            tmp.append(copy.deepcopy(el))   # do tablicy tymczasowej dodajemy kopie zbioru z tablicy wynikowej
            #print(tmp)
            tmp[-1].append(tab[i])     #do ostatnio dodanego zbioru dodajemy nowy element
        for el2 in tmp:
            results.append(el2)         #dodajemy elementy z tablicy tymczasowej do tablicy z wynikami
        tmp = []                       #zerujemy tablice wynikowa

    return results
</code>

** Złożoność: ** 
**$\mathcal{O}(2^n)$**
| ''n'' | ''liczba wszystkich wierzchołków''|

==== Algorytm pełnego przeglądu grafu w celu poszukiwania rozwiązań ====

^ Dane ^ Opis ^
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''matrix''  | ''macierz sąsiedztwa''|
| ''vertices_list'' | ''lista z wierzchołkami''|
| ''sets'' | ''lista ze wszystkimi podzbiorami grafu''|
| ''test_results'' | ''lista z odpowiedziami, czy zbiór pokrywa graf (True/False)''|
| ''test_result'' | ''pojedyńcza odpowiedź, czy zbiór pokrywa graf (True/False)''|

<code python>
def full_graph_cover_test(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)
    sets = power_set(vertices_list, vertexAmount)

    test_results = []
    best_solutions = []
    shortest_length = vertexAmount

    for set in sets:
        test_result = graph_cover_test(vertexAmount, matrix, set)
        if test_result == True:
            if len(set)<=shortest_length:
                best_solutions.append(set)
                shortest_length=len(set)
        test_results.append(test_result)


    print("Sets and results:")
    print(sets)
    print(test_results)

    return  best_solutions
</code>

**Złożoność:**
**$\mathcal{O}(2^n \cdot n^3)$** → każdy podzbiór musi być sprawdzony
| ''n'' | ''liczba wszystkich wierzchołków''|

 
=== Sposób z użyciem mniejszej ilości pamięci (optymalizacja związana z podzbiorami) ===
<code python>
import itertools

def full_graph_cover_test2(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)

    test_results = []
    best_solutions = []
    shortest_length = vertexAmount

    for i in range(vertexAmount):
        sets = itertools.combinations(vertices_list,i)
        for set in sets:
            test_result = graph_cover_test(vertexAmount, matrix, set)
            if test_result == True:
                if len(set) <= shortest_length:
                    best_solutions.append(set)
                    shortest_length = len(set)
            test_results.append(test_result)

    print("Results:")
    #print(power_set(vertices_list,vertexAmount)) #Opcjonalnie do wglądu w podzbiory
    print(test_results)

    return  best_solutions
</code>


==== Wykresy czasów wykonania ====
Wszystkie wykresy zostały wykonane dla próbki danych liczącej **100** różnych grafów dla każdej liczby wierzchołków N.

=== Czas wykonania (w sekundach) pełnego przeglądu grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.25: ===
{{ :ok20:pr013:p145392:wykres25.png?600 |}}

=== Czas wykonania (w sekundach) pełnego przeglądu grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.5: ===
{{ :ok20:pr013:p145392:wykres50.png?600 |}}

=== Czas wykonania (w sekundach) pełnego przeglądu grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.75: ===
{{ :ok20:pr013:p145392:wykres75.png?600 |}}

==== Wykresy średniej wielkości dobrego zbioru (takiego, który pokrywa graf) ====

=== Średnia wielkość dobrego zbioru grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.25: ===
{{ :ok20:pr013:p145392:zbior25.png?600 |}}

=== Średnia wielkość dobrego zbioru grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.5: ===
{{ :ok20:pr013:p145392:zbior50.png?600 |}}

=== Średnia wielkość dobrego zbioru grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.75: ===
{{ :ok20:pr013:p145392:zbior75.png?600 |}}

=== Zbiórczy wykres średnich wielkości dobrego zbioru dla wszystkich wyżej wymienionych prawdopodobieństw p: ===
{{ :ok20:pr013:p145392:zbiory.png?600 |}}

===== Algorytm prezentujący rozwiązanie przybliżone =====
Na podstawie pomiarów średniego zbioru pokrywającego graf przeprowadzonych na ''Algorytmie pełnego przeglądu podzbiorów'' i regresji przeprowadzonych na uzyskanych wynikach otrzymaliśmy wzór na średnią wielkość pokrywającego podzbioru. Następnie przegląd podzbiorów zaczynamy od podzbiorów o wyliczonej wcześniej wartości. Kończymy po odnalezieniu pierwszego rozwiązania.

**To rozwiązanie zwraca optymalne, choć nie zawsze najlepsze rozwiązanie**

^ Dane ^ Opis ^
| ''matrix'' | ''macierz sąsiedztwa'' |
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''p'' | ''prawdopodobieństwo z jakim tworzono krawędzie w grafie'' |
| ''vertices''  | ''wszystkie wierzchołki podane w jednej liście''|
| ''minimalLength'' | ''zaokrąglona w górę wyliczona średnia wielkość pokrywającego podzbioru'' |
| ''subsets'' | ''podzbiory grafu o podanej wielkości'' |

<code python>
import itertools
import math

def Aproximated_graph_cover_test(matrix, vertexAmount, p):
    vertices = []
    for vertex in range(vertexAmount):
        vertices.append(vertex)
    if p == 0.25:
        minimalLength = math.ceil(0.431698449296429 * vertexAmount + 1.28057012910952)
    elif p == 0.5:
        minimalLength =  math.ceil(0.467252521696703 * vertexAmount + 0.490780704345053)
    elif p == 0.75:
        minimalLength =   math.ceil(0.476384874362637 * vertexAmount + 0.351959433901099)
    else:
        print("Wybrano nieprawidłowe p \n")
        exit(1)
    for amount in range(minimalLength,vertexAmount+1):
        subsets = itertools.combinations(vertices,amount)
        for subset in subsets:
            if (graph_cover_test(vertexAmount,matrix,subset) == True):
                return subset
</code>

**Średnia złożoność:**

**$\mathcal{O}(n^3)$** → zazwyczaj algorytm przechodzi tylko kilka pętli


**Złożoność pesymistyczna:**

**$\mathcal{O}(m \cdot n^3)$** → $\mathcal{O}(n^4)$

**$m = 2^n - 2^{\lfloor w \rfloor}$**

| ''w'' | ''wyliczona średnia wartość dobrego podzbioru'' |
| ''n'' | ''liczba wszystkich wierzchołków''|
| ''m'' | ''maksymalna liczba podzbiorów, które mogą sprawdzone w tym algorytmie'' | 
====== Wizualizacja z użyciem GraphViz ======
Aby móc uruchamiać poniższe algorytmy trzeba do projektu dodać bibliotekę **graphviz**
===== Instalacja GraphViz =====
  - Pobrać oprogramowanie GraphViz z [[https://graphviz.org/download/]]
  - Dodać ścieżkę do folderu "bin" oprogramowania GraphViz do zmiennej środowiskowej "Path".
  
Przykład:
     "C:\Program Files (x86)\Graphviz2.38\bin"
     
Polecam korzystać z wersji 2.38, dla wersji nowszych/niekompletnych wizualizacja może nie zadziałać.
    
Link do bezpośredniego pobrania (pochodzi ze skryptu używanego przy pobieraniu za pomocą ''winget'' ) : https://graphviz.gitlab.io/_pages/Download/windows/graphviz-2.38.msi 
     
**Uwaga!** Gdyby przy kompilacji kodu nastąpił błąd:

     "graphviz.backend.executablenotfound: failed to execute ['circo', '-tpng', '-o', 'graph.gv'], make sure the graphviz executables are on your systems' path"
     
należy do zmiennej środowiskowej "Path" dodać ścieżkę bezpośrednio do pliku "circo.exe" oprogramowania Graphviz.
     Przykład:
     "C:\Program Files (x86)\Graphviz2.38\bin\circo.exe"


===== Generowanie grafów =====

[[https://pw20we.cs.put.poznan.pl/doku.php?id=ok:modele_grafow_losowych]]
<code python>
def gnp(n, p):
    "Model G(n,p)"
    a = [[0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if (random.random() <= p):
                a[i][j] = a[j][i] = 1
    return a
</code>


===== Weryfikacja poprawności rozwiązania =====

^ Dane ^ Opis ^
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''matrix''  | ''macierz sąsiedztwa''|
| ''answers'' | ''rozwiązanie poddawane weryfikacji''|
| ''matrix_to_graphViz'' | ''zmodyfikowana tablica sąsiadów, która przyda się przy wizualizacji testu''|
| ''check_table'' | ''tablica z 0 i 1 informująca czy wierzchołek(indeks) został pokryty(1), czy nie(0)''|
| ''correctly_covered'' | ''zmienna boolowska informująca czy rozwiązanie jest prawidłowe''|

<code python>
from copy import deepcopy

def graph_cover_test_graphViz(vertexAmount,matrix,answers):
    matrix_to_graphViz=deepcopy(matrix)
    check_table=[]
    for i in range(vertexAmount):
        check_table.append(0)
    for answer in answers:
        check_table[answer] = 1
        for i in range(vertexAmount):
            if matrix[answer][i] == 1:
                check_table[i]=1
                matrix_to_graphViz[answer][i]= 2        #2 - krawędź z pierwszym sąsiadem
                matrix_to_graphViz[i][answer]= 2
                for j in range(vertexAmount):
                    if matrix[i][j] == 1:
                        check_table[j]=1
                        if matrix_to_graphViz[i][j]!=2:
                            matrix_to_graphViz[i][j] = 3     # 3 -krawędź z drugim sąsiadem
                            matrix_to_graphViz[j][i] = 3
    not_covered = []
    for e in range(vertexAmount):
        if check_table[e] != 1:
            not_covered.append(e)
    if len(not_covered) > 0:
        print("Wrong covered: " + str(not_covered))
        correctly_covered = False
    else:
        print("Correctly covered.")
        correctly_covered = True
    return correctly_covered,not_covered,matrix_to_graphViz
</code>
===== Prezentacja testu z użyciem oprogramowania GraphViz=====

^ Dane ^ Opis ^
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''matrix_to_graphViz'' | ''zmodyfikowana tablica sąsiadów, która przyda się przy wizualizacji testu''|
| ''answers'' | ''rozwiązanie poddawane weryfikacji''|
| ''not_covered'' | ''lista niepokrytych wierzchołków''|
| ''file_number'' | ''numer dopisany do "Graph" w nazwie plików wyjściowych''|
| ''display'' | '' graf''|
| ''answer'' | ''zmienna boolowska informująca czy wierzchołek był w rozwiązaniu''|
| ''uncovered'' | ''zmienna boolowska informująca czy wierzchołek nie został przykryty''|


<code python>
import graphviz


def display_cover_test_in_graphViz(vertexAmount,matrix_to_graphViz,answers,not_covered,filenumber):
    display = graphviz.Graph(engine='circo',filename="Graph"+str(filenumber)) #inicjalizacja i nadanie nazwy plikom
    for vertex in range(vertexAmount):
        answer = False
        uncovered = False

        if vertex in not_covered:
            uncovered = True
        if vertex in answers:
            answer = True
        if uncovered:
            display.node(str(vertex), str(vertex), color='red')    #dodanie wierzchołka niepokrytego do grafu
        elif answer:
            display.node(str(vertex), str(vertex), color='green')     #dodanie wierzchołka z rozwiązania do grafu
        else:
            display.node(str(vertex), str(vertex))    #dodanie innych wierzchołków do grafu

    for i in range(vertexAmount - 1):
        for j in range(i, vertexAmount):
            if matrix_to_graphViz[i][j] == 1:
                display.edge(str(i), str(j), constraint='false')     #dodanie zwykłej krawędzi do grafu
            elif matrix_to_graphViz[i][j] == 2:
                display.edge(str(i), str(j), constraint='false', color='green')     #dodanie krawędzi połączenia z pierwszym sąsiadem wierzchołka z rozwiązania do grafu
            elif matrix_to_graphViz[i][j] == 3:
                display.edge(str(i), str(j), constraint='false', color='yellow')     #dodanie krawędzi połączenia z drugim sąsiadem wierzchołka z rozwiązania do grafu
    # print(display.source)             # kod w GraphViz
    display.render( format='png')              # generuje plik z kodem do Graphviz i plik png z wizualizacją testu
    #display.render(view='true', format='png')   # to co wyżej + otwiera plik png do podgladu
</code>



===== Algorytm zachłanny =====
==== Pomocniczy algorytm zliczający moc pokrycia każdego z wierzchołków ====
^ Dane ^ Opis ^
| ''matrix''  | ''macierz sąsiedztwa''|
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''covered'' | ''tablica z 0 i 1 informująca czy wierzchołek(indeks) został pokryty(1), czy nie(0)'' |
| ''vertices'' | ''słownik numerów wierzchołków i ilością wierzchołów, które mogą one pokryć'' |
| ''check_table'' | ''tablica z 0 i 1 informująca czy w danym przejściu pętli wierzchołek(indeks) został policzony jako możliwy do pokrycia(1), czy też nie(0)''|

<code python>
def Connection_counter(matrix,vertexAmount,covered):
    vertices={}
    for vertex in range(vertexAmount):
        vertices[vertex] = 0

    for i in range(vertexAmount):
        check_table = [0 for _ in range(vertexAmount)]
        check_table[i] = 1
        for j in range(vertexAmount):
            if matrix[i][j]==1:
                if check_table[j] == 0:
                    if covered[j] == 0:
                        vertices[i]+=1
                    check_table[j] = 1
                for m in range(vertexAmount):
                    if matrix[j][m] == 1:
                        if check_table[m] == 0:
                            if covered[m] == 0:
                                vertices[i]+=1
                            check_table[m] = 1

    return vertices

</code>


==== Właściwy algorytm zachłanny ====
^ Dane ^ Opis ^
| ''matrix''  | ''macierz sąsiedztwa''|
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''matrix_copy'' | ''kopia właściwej macierzy, na której są przeprowadzane działania usuwania polączeń'' |
| ''covered'' | ''tablica z 0 i 1 informująca czy wierzchołek(indeks) został pokryty(1), czy nie(0)'' |
| ''vertices'' | ''słownik numerów wierzchołków i ilością wierzchołów, które mogą one pokryć'' |
| ''solution'' | ''tablica wierzchołków, które pokrywają cały graf'' |
| ''test_result'' | ''zmienna boolowska, informuje czy "solution" pokryło graf i można zakończyć algorytm(True), czy nie(False)'' |
| ''ordered_vertices'' | ''posortowane wierzchołki - od najwięcej niepokrytych wierzchołków pokrywającego do najmniej '' | 
| ''best_one'' | ''wierzchołek, który w danej sytuacji pokrywa najwięcej niepokrytych wierzchołków'' |
| ''not_covered'' | ''tablica zawierająca wierzchołki, których "solution" nie pokrywa'' |
| ''matrix_to_graphViz'' | ''zmodyfikowana macierz, przyda się przy wizualizacji rozwiązania'' |

<code python>
import copy


def Greedy_graph_cover_test(matrix,vertexAmount):
    matrix_copy=copy.deepcopy(matrix)

    covered = [0 for _ in range(vertexAmount)]

    vertices = Connection_counter(matrix,vertexAmount,covered)

    solution = []
    test_result = False

    while not test_result:
        ordered_vertices = sorted(vertices, key=vertices.get, reverse=True)
        best_one = ordered_vertices[0]
        while vertices[best_one] == 0 and covered[best_one] == 1:
            vertices.pop(best_one)
            best_one = ordered_vertices[0]
        solution.append(best_one)

        for i in range(vertexAmount):
            if matrix_copy[best_one][i]==1:
                matrix_copy[best_one][i] = 0
                matrix_copy[i][best_one] = 0
                for j in range(vertexAmount):
                    if matrix_copy[i][j] == 1:
                        matrix_copy[i][j] = 0
                        matrix_copy[j][i] = 0

        test_result,not_covered,matrix_to_graphViz = graph_cover_test_graphViz(vertexAmount,matrix,solution)

        covered = [1 for _ in range(vertexAmount)]

        for vertex in not_covered:
            covered[vertex] = 0

        vertices = Connection_counter(matrix_copy, vertexAmount,covered)



    display_cover_test_in_graphViz(vertexAmount, matrix_to_graphViz, solution, not_covered, 1)
    return solution
</code>



===== Algorytm przeszukujący wszystkie podzbiory (Brute Force) =====
==== Algorytm tworzący zbiór potęgowy grafu ====

^ Dane ^ Opis ^
| ''tab'' | ''lista z wierzchołkami'' |
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''results''  | ''lista ze wszystkimi podzbiorami grafu''|


<code python>
import copy
#1. Tworzymy tablice wynikowa, z jednym zbiorem pustym
#2. Przechodzimy po elementach tablicy wejsciowej
#3. Dla kazdego zbioru z tablicy wynikowej tworzymy kopie
#4. Nastepnie dodajemy do niej element z tablicy wejsciowej
#4. Nowo powstale zbior dodajemy do puli zbiorow w tablicy wynikowej
#5. Kroki te powtarzamy, az nie skoncza nam sie elementy tablicy wejsciowej

def power_set(tab,vertexAmount):
    results = [[]]                           #przygotowanie tablicy na wyniki
    tmp = []                                #tablica tworzaca kolejne zbior
    # dla kazdego elementu zbioru wejsciowego
    # przechodzimy elementy tablicy z wynikami
    for i in range(vertexAmount):
        for el in results:
            tmp.append(copy.deepcopy(el))   # do tablicy tymczasowej dodajemy kopie zbioru z tablicy wynikowej
            #print(tmp)
            tmp[-1].append(tab[i])     #do ostatnio dodanego zbioru dodajemy nowy element
        for el2 in tmp:
            results.append(el2)         #dodajemy elementy z tablicy tymczasowej do tablicy z wynikami
        tmp = []                       #zerujemy tablice wynikowa

    return results
</code>


==== Algorytm pełnego przeglądu grafu w celu poszukiwania rozwiązań ====

^ Dane ^ Opis ^
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''matrix''  | ''macierz sąsiedztwa''|
| ''vertices_list'' | ''lista z wierzchołkami''|
| ''sets'' | ''lista ze wszystkimi podzbiorami grafu''|
| ''test_results'' | ''lista z odpowiedziami, czy zbiór pokrywa graf (True/False)''|
| ''test_result'' | ''pojedyńcza odpowiedź, czy zbiór pokrywa graf (True/False)''|
| ''for_graphViz_to_display'' | ''lista zmodyfikowanych macierzy, przydatnych w wizualizacji rozwiązań''|
| ''matrix_to_graphViz'' | ''zmodyfikowana macierz, przyda się przy wizualizacji rozwiązania''|
| ''not_covered_list'' | ''lista z listami niepokrytych wierzchołków''|
| ''not_covered'' | ''lista niepokrytych wierzchołków''|

<code python>
def full_graph_cover_test(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)
    sets = power_set(vertices_list, vertexAmount)

    test_results = []
    for_graphViz_to_display = []
    not_covered_list = []

    best_solutions = []
    shortest_length = vertexAmount

    for e in sets:
        test_result, not_covered, matrix_to_graphViz = graph_cover_test_graphViz(vertexAmount, matrix, e)
        if test_result == True:
            print("xd")
            if len(e) <= shortest_length:
                best_solutions.append(e)
                for_graphViz_to_display.append(matrix_to_graphViz)
                not_covered_list.append(not_covered)
                shortest_length = len(e)
        test_results.append(test_result)


    print("Sets and results:")
    print(sets)
    print(test_results)

    for e in range(len(best_solutions)):
        display_cover_test_in_graphViz(vertexAmount, for_graphViz_to_display[e], best_solutions[e], not_covered_list[e], e)


    return  best_solutions
</code>

=== Sposób z użyciem mniejszej ilości pamięci (optymalizacja związana z podzbiorami) ===

<code python>
import itertools

def full_graph_cover_test2(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)


    test_results = []
    for_graphViz_to_display = []
    not_covered_list = []

    best_solutions = []
    shortest_length = vertexAmount

    for i in range(vertexAmount):
        sets = itertools.combinations(vertices_list,i)
        for e in sets:
            test_result, not_covered, matrix_to_graphViz = graph_cover_test_graphViz(vertexAmount, matrix, e)
            if test_result == True:
                if len(e) <= shortest_length:
                    best_solutions.append(e)
                    for_graphViz_to_display.append(matrix_to_graphViz)
                    not_covered_list.append(not_covered)
                    shortest_length = len(e)
            test_results.append(test_result)


    print("Results:")
    # print(power_set(vertices_list,vertexAmount)) #Opcjonalnie do wglądu w podzbiory
    print(test_results)

    for e in range(len(best_solutions)):
        display_cover_test_in_graphViz(vertexAmount, for_graphViz_to_display[e], best_solutions[e], not_covered_list[e], e)

    return best_solutions
</code>

===== Algorytm prezentujący rozwiązanie przybliżone =====
^ Dane ^ Opis ^
| ''matrix''  | ''macierz sąsiedztwa''|
| ''vertexAmount'' | ''liczba wierzchołków w grafie'' |
| ''p'' | ''prawdopodobieństwo z jakim tworzono krawędzie w grafie'' |
| ''vertices''  | ''wszystkie wierzchołki podane w jednej liście''|
| ''minimal_length'' | ''zaokrąglona w górę wyliczona średnia wielkość pokrywającego podzbioru'' |
| ''subsets'' | ''podzbiory grafu o podanej wielkości'' |
| ''not_covered'' | ''lista niepokrytych wierzchołków''|
| ''matrix_to_graphViz'' | ''zmodyfikowana macierz, przyda się przy wizualizacji rozwiązania''|
| ''test_result'' | ''zmienna boolowska, czy dany zbiór pokrywa graf (True/False)''|



<code python>
import itertools
import math

def Aproximated_graph_cover_test(matrix, vertexAmount, p):
    vertices = []
    for vertex in range(vertexAmount):
        vertices.append(vertex)
    if p == 0.25:
        minimal_length = math.ceil(0.431698449296429 * vertexAmount + 1.28057012910952)
    elif p == 0.5:
        minimal_length =  math.ceil(0.467252521696703 * vertexAmount + 0.490780704345053)
    elif p == 0.75:
        minimal_length =   math.ceil(0.476384874362637 * vertexAmount + 0.351959433901099)
    else:
        print("Wybrano nieprawidłowe p \n")
        exit(1)
    for amount in range(minimal_length,vertexAmount+1):
        subsets = itertools.combinations(vertices,amount)
        for subset in subsets:
            test_result,not_covered,matrix_to_graphViz = graph_cover_test(vertexAmount,matrix,subset)
            if ( test_result == True):
                display_cover_test_in_graphViz(vertexAmount, matrix_to_graphViz, subset, not_covered, 2)
                return subset
</code>

