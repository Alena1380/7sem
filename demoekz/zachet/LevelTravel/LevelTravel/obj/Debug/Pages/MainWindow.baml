   M S B A M L   `   `   `  ????B  >WpfApp1, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null!clr-namespace:WpfApp1WpfApp1  5   	       WpfApp1.MainWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   'localclr-namespace:WpfApp1     5   	     ? Title$  LevelTravel??5   	   $
??1000??6   $	??800??6.   .??5	      ? ??5
   
   ?? 5       ?? EndPoint$ 0.5,1&?6"    ?? 
StartPoint$ 0.5,0&?63    ?? RelativeTransform 5      V? 5      .~?5      ??  ?? CenterY$	 0.5Q?6)    ?? CenterX$	 0.5Q?67   ?? 5       ?? CenterX$	 0.5Q?6(    ?? CenterY$	 0.5Q?66   ?? 5       ?? Angle$	 -90Q?6*   	 ?? CenterX$		 0.5Q?66   
 ?? CenterY$	
 0.5Q?6D   T? 5      5      .??5      ?  ? Color$	 Red??6   ? 5      $ 	#FF9400FF??6    ? Offset$ 1Q?61   ? 5      $ 	#FFFFA400??6   $ 0.282Q?61   ? 5      $ 	#FF00EDFF??6   $
 0.71Q?61   ? 5      $ 	#FF88FF00??6   $ 0.568Q?61   ? 5      $ 	#FFFFF500??6   $ 0.426Q?61   ? 5      $ 	#FF0004FF??6   $ 0.852Q?61   5       ? RowDefinitions 5   
   ?? 5      $??75 ?6   ?? 5      $??0* ?6   ?? 5       $	??30* ?6   .+?5"   
   ?? $2??,/WpfApp1;component/Resources/leveltravel.jpg??6   $
??Left=?6F   $	??133??6a   $??0,0,0,13q?6m    J? OpacityMask 5#      ?? 5$       ?? ImageSource$  /Resources/leveltravel.jpg??6    j? Stretch$
 None=?6F   5&      ?? 5(   
   -   5        $??BtnBack??5(   !   $??
Назад??6   $	??175??60   $??30??6<   $??Right=?6H   
??????????	#FF54ADFF6?   ?? 5)   
   $??Level.Travel??6   $??48(?6(   $
??Left=?66   $??Center=?6Q   $??75??6l   $??67,0,0,0q?6x   $	??350??6?   $??MV Boli)?6?   
???   ?6?   ? 5*   
    K? ZIndex$ -2??6   $??89??6!   $??Center=?6-   
???????6H   ? 5+   
   ???#2DCDCD$??2??6$   $??1??65    ? 5,   
   -   5        $??	MainFrame??5,   ]     ? NavigationUIVisibility$ Hidden=?6   $??3??6n   $??0,76,0,0q?6   ??5-      ?? 5.      $$ /Resources/leveltravelmain.jpg??6   ??50      ?? 51      53      55      56      