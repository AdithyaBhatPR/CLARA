
    #include<stdio.h>
    main()
    {
    int a[100],i,n,j,ev=0,od=0;
    scanf("%d",&n);
    	for (i=0;i<n;i++)
    	{	scanf("%d",&a[i]);
    		if (a[i]%2==0) ev++;
    		else od++;
    	}
    	if (ev>od) printf("READY FOR BATTLE");
    	else printf("NOT READY");
    	return 0;
    }

