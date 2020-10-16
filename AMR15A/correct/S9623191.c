
    #include<stdio.h>
    main()
    {
    int a[100],i,n,ev=0;
    scanf("%d",&n);
    	for (i=0;i<n;i++)
    	{	scanf("%d",&a[i]);
    		if (a[i]%2==0) ev++;
    	}
    	if (ev>n-ev) printf("READY FOR BATTLE");
    	else printf("NOT READY");
    	return 0;
    } 

