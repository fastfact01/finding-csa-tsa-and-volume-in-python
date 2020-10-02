#this prgram is a calculater of c.s.a,t.s.a and vol. of 3d shapes
#by rohit singh class 11 sci
#version1.0
#based on maths formule
def T_S_A():
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("wlecome to T.S.A finder:>")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("select a shape from given below and write code \n ------for example type cube for TSA of cube------ \n  #>cube for 3dshape cube \n  #>cuboid for 3dshape cuboid \n  #>cone for 3dshape cone \n  #>cylinder for 3dshape cylinder")
	print("  #>sphare for 3dshape sphare \n  #>hemisphare for 3dshape hemisphare \n  #>frustum for 3dshape frustum of cone \n  #>hollow cylinder for 3dshape hollow cylinder \n")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("note-- please left a space between hollow and cylinder::")
	print("       please write the name of shape correctely!")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	a=input("enter the code:>")
	print("---------------------------------------------------")
	if a.capitalize()=="Cube":
		edge_t_s_a_=float(input("enter edge of cube:>"))
		rohit=edge_t_s_a_*edge_t_s_a_
		print("the T.S.A of Cube is:>",6*rohit)
	elif a.capitalize()=="Cuboid":
		len_T_S_A_=float(input("enter length of Cuboid:>"))
		bre_T_S_A_=float(input("enter brith of Cuboid:>"))
		hight_cuboid_tsa=float(input("enter hight of Cuboid:>"))
		lb=len_T_S_A*bre_T_S_A_
		bh=bre_T_S_A_*hight_cuboid_tsa
		hl=hight_cuboid_tsa*len_T_S_A_
		total_cuboid_tsa=lb+bh+hl
		print("the T.S.A of Cuboid is:>",2*total_cuboid_tsa)
	elif a.capitalize()=="Cylinder":
		radius_T_S_A_CYL=float(input("enter radius of Cylinder:>"))
		hight_tsa_Cyl=float(input("enter hight of Cylinder:>"))
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n note-->please write the option not the value! ")
		pi_for_tsa_of_cyl=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_cyl.capitalize()=="A":
			#2πr(h+r)
			h_plus_r_tsa=hight_tsa_Cyl+radius_T_S_A_CYL
			cyl_pie_tsa=22/7
			print("the T.S.A of Cylinder is:>",2*cyl_pie_tsa*radius_T_S_A_CYL*h_plus_r_tsa)
		elif pi_for_tsa_of_cyl.capitalize()=="B":
			h_plus_r_tsa=hight_tsa_Cyl+radius_T_S_A_CYL
			cyl_pie_tsa=3.14
			print("the T.S.A of Cylinder is:>",2*cyl_pie_tsa*radius_T_S_A_CYL*h_plus_r_tsa)
		elif pi_for_tsa_of_cyl.capitalize()=="C":
			h_plus_r_tsa=hight_tsa_Cyl+radius_T_S_A_CYL
			cyl_pie_tsa=3.141
			print("the T.S.A of Cylinder is:>",2*cyl_pie_tsa*radius_T_S_A_CYL*h_plus_r_tsa)	
		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Cone":
		#πr(l+r)
		radius_T_S_A_Cone=float(input("enter the radius of Cone:>"))
		slant_tsa_Cone=float(input("enter the slant hight of Cone:>"))
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n note--please write the option not the value!")
		pi_for_tsa_of_cone=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_cone.capitalize()=="A":
			#2πr(h+r)
			l_plus_r_tsa=slant_tsa_Cone+radius_T_S_A_Cone
			cone_pie_tsa=22/7
			print("the T.S.A of Cone is:>",cone_pie_tsa*radius_T_S_A_Cone*l_plus_r_tsa)
		elif pi_for_tsa_of_cone.capitalize()=="B":
			l_plus_r_tsa=slant_tsa_Cone+radius_T_S_A_Cone
			cone_pie_tsa=3.14
			print("the T.S.A of Cone is:>",cone_pie_tsa*radius_T_S_A_Cone*l_plus_r_tsa)
		elif pi_for_tsa_of_cone.capitalize()=="C":
			l_plus_r_tsa=slant_tsa_Cone+radius_T_S_A_Cone
			cone_pie_tsa=3.141
			print("the T.S.A of Cone is:>",cone_pie_tsa*radius_T_S_A_Cone*l_plus_r_tsa)	
		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Sphare":
		#4π(r*r)
		radius_sphare_TSA=float(input("enter the radius of sphare:>"))
		r2_sphare_tsa=radius_sphare_TSA*radius_sphare_TSA
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value! ")
		pi_for_tsa_of_sphare=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_sphare.capitalize()=="A":
			
			sphare_pie_tsa=22/7
			print("The TSA of Sphare is not possible scientifically but by using 4π(rxr) the answer is:>",4*sphare_pie_tsa*r2_sphare_tsa)

		elif pi_for_tsa_of_sphare.capitalize()=="B":
			sphare_pie_tsa=3.14
			print("The TSA of Sphare is not possible scientifically but by using 4π(rxr) the answer is:>",4*sphare_pie_tsa*r2_sphare_tsa)

		elif pi_for_tsa_of_sphare.capitalize()=="C":
			sphare_pie_tsa=3.141
			print("The TSA of Sphare is not possible scientifically but by using 4π(rxr) the answer is:>",4*sphare_pie_tsa*r2_sphare_tsa)

		else:
			print("please write the option not the value!!")
	elif a.capitalize()=="Hemisphare":
	#2π(r*r)
		radius_hemisphare_TSA=float(input("enter the radius of hemisphare:>"))
		r2_hemisphare_tsa=radius_hemisphare_TSA*radius_hemisphare_TSA
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_hemisphare=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_hemisphare.capitalize()=="A":
			#3πr(r*r)
			hemisphare_pie_tsa=22/7
			print("The TSA of hemiSphare is :>",3*hemisphare_pie_tsa*r2_hemisphare_tsa)

		elif pi_for_tsa_of_hemisphare.capitalize()=="B":
			hemisphare_pie_tsa=3.14
			print("The TSA of HemiSphare is :>",3*hemisphare_pie_tsa*r2_hemisphare_tsa)

		elif pi_for_tsa_of_hemisphare.capitalize()=="C":
			hemisphare_pie_tsa=3.141
			print("The TSA of HemiSphare is :>",3*hemisphare_pie_tsa*r2_hemisphare_tsa)

		else:
			print("please write the option not the value!!")
	elif a.capitalize()=="Frustum":
		slant_tsa_Frustum=float(input("enter slant hight of Frustum:>"))
		r1_frustum_tsa=float(input("enter frist radius of Frustum:>"))
		r2_frustum_tsa=float(input("enter second radius of Frustum:>"))
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value! ")
		pi_for_tsa_of_Frustum=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_Frustum.capitalize()=="A":
			#πl(r1+r2)+πr1^2+πr2^2
			r1_plus_r2_tsa=r1_frustum_tsa+r2_frustum_tsa
			Frustum_pie_tsa=22/7
			ar12=r1_frustum_tsa*r1_frustum_tsa
			ar1=Frustum_pie_tsa*ar12
			ar22=r2_frustum_tsa*r2_frustum_tsa
			ar2=Frustum_pie_tsa*ar22

			print("the T.S.A of Frustum is:>",Frustum_pie_tsa*slant_tsa_Frustum*r1_plus_r2_tsa+ar1+ar2)
		elif pi_for_tsa_of_Frustum.capitalize()=="B":
			r1_plus_r2_tsa=r1_frustum_tsa+r2_frustum_tsa
			Frustum_pie_tsa=3.14
			ar12=r1_Frustum_tsa*r1_frustum_tsa
			ar1=frustum_pie_tsa*ar12
			ar22=r2_frustum_tsa*r2_frustum_tsa
			ar2=Frustum_pie_tsa*ar22
			
			print("the T.S.A of Frustum is:>",Frustum_pie_tsa*slant_tsa_Frustum*r1_plus_r2_tsa+ar1+ar2)
		elif pi_for_tsa_of_Frustum.capitalize()=="C":
			r1_plus_r2_tsa=r1_frustum_tsa+r2_frustum_tsa
			Frustum_pie_tsa=3.14
			ar12=r1_Frustum_tsa*r1_frustum_tsa
			ar1=frustum_pie_tsa*ar12
			ar22=r2_frustum_tsa*r2_frustum_tsa
			ar2=Frustum_pie_tsa*ar22
			
			print("the T.S.A of Frustum is:>",Frustum_pie_tsa*slant_tsa_Frustum*r1_plus_r2_tsa+ar1+ar2)
		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Hollow cylinder":	
		# 2π ( r1 + r2 )( r2 - r1 +h)
		r1hollowtsa=float(input("enter the inner radius of hollow cylinder:>"))
		r2hollowtsa=float(input("enter outer radius:>"))
		hofhollowtsa=float(input("enter hight of cylinder:>"))
		r1_plus_r2hollow_tsa=r1hollowtsa+r2hollowtsa
		r2_minus_r1_plus_h=r2hollowtsa-r1hollowtsa+hofhollowtsa
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pie_for_hollo_tsa=input("enter the option....for eg.a,b&c")
		if pie_for_hollo_tsa.capitalize()=="A":
			pie___=22/7
			print("the TSA of hollow cylinder is:>",2*pie___*r1_plus_r2hollow_tsa*r2_minus_r1_plus_h)
		if pie_for_hollo_tsa.capitalize()=="B":
			pie___=3.14
			print("the TSA of hollow cylinder is:>",2*pie___*r1_plus_r2hollow_tsa*r2_minus_r1_plus_h)
		if pie_for_hollo_tsa.capitalize()=="C":
			pie___=3.141
			print("the TSA of hollow cylinder is:>",2*pie___*r1_plus_r2hollow_tsa*r2_minus_r1_plus_h)
		else:
			print("please write the option not the value!")
	else:
		print("invalid input!")

def C_S_A():
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("wlecome to C.S.A finder:>")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("select a shape from given below and write code \n ------for example type cube for CSA of cube------ \n  #>cube for 3dshape cube \n  #>cuboid for 3dshape cuboid \n  #>cone for 3dshape cone \n  #>cylinder for 3dshape cylinder")
	print("  #>sphare for 3dshape sphare \n  #>hemisphare for 3dshape hemisphare \n  #>frustum for 3dshape frustum of cone \n  #>hollow cylinder for 3dshape hollow cylinder \n")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("note-- please left a space between hollow and cylinder::")
	print("       please write the name of shape correctely!")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	a=input("enter the code:>")
	print("---------------------------------------------------")
	if a.capitalize()=="Cube":
		edge_t_s_a_=float(input("enter edge of cube:>"))
		rohit=edge_t_s_a_*edge_t_s_a_
		print("the C.S.A of Cube is:>",4*rohit)
	elif a.capitalize()=="Cuboid":
		len_T_S_A_=float(input("enter length of Cuboid:>"))
		bre_T_S_A_=float(input("enter brith of Cuboid:>"))
		hight_cuboid_tsa=float(input("enter hight of Cuboid:>"))
		l_plus_b=len_T_S_A_+bre_T_S_A_
		into_h=l_plus_b*hight_cuboid_tsa
		print("the C.S.A of Cuboid is:>",2*into_h)
	elif a.capitalize()=="Cylinder":
		radius_T_S_A_CYL=float(input("enter radius of Cylinder:>"))
		hight_tsa_Cyl=float(input("enter hight of Cylinder:>"))
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_cyl=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_cyl.capitalize()=="A":
			#2πrh
			cyl_pie_tsa=22/7
			print("the C.S.A of Cylinder is:>",2*cyl_pie_tsa*radius_T_S_A_CYL*hight_tsa_Cyl)
		elif pi_for_tsa_of_cyl.capitalize()=="B":
			cyl_pie_tsa=3.14
			print("the C.S.A of Cylinder is:>",2*cyl_pie_tsa*radius_T_S_A_CYL*hight_tsa_Cyl)
		elif pi_for_tsa_of_cyl.capitalize()=="C":
			cyl_pie_tsa=3.141
			print("the C.S.A of Cylinder is:>",2*cyl_pie_tsa*radius_T_S_A_CYL*hight_tsa_Cyl)	
		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Cone":
		#πrl
		radius_T_S_A_Cone=float(input("enter the radius of Cone:>"))
		slant_tsa_Cone=float(input("enter the slant hight of Cone:>"))
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_cone=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_cone.capitalize()=="A":
			cone_pie_tsa=22/7
			print("the C.S.A of cone is:>",cone_pie_tsa*radius_T_S_A_Cone*slant_tsa_Cone)
		elif pi_for_tsa_of_cone.capitalize()=="B":
			cone_pie_tsa=3.14
			print("the C.S.A of cone is:>",cone_pie_tsa*radius_T_S_A_Cone*slant_tsa_Cone)
		elif pi_for_tsa_of_cone.capitalize()=="C":
			cone_pie_tsa=3.141
			print("the C.S.A of cone is:>",cone_pie_tsa*radius_T_S_A_Cone*lslant_tsa_Cone)	
		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Sphare":
		#4π(r*r)
		radius_sphare_TSA=float(input("enter the radius of sphare:>"))
		r2_sphare_tsa=radius_sphare_TSA*radius_sphare_TSA
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_sphare=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_sphare.capitalize()=="A":
			
			sphare_pie_tsa=22/7
			print("The CSA of Sphare is :>",4*sphare_pie_tsa*r2_sphare_tsa)

		elif pi_for_tsa_of_sphare.capitalize()=="B":
			sphare_pie_tsa=3.14
			print("The CSA of Sphare is :>",4*sphare_pie_tsa*r2_sphare_tsa)

		elif pi_for_tsa_of_sphare.capitalize()=="C":
			sphare_pie_tsa=3.141
			print("The CSA of Sphare is :>",4*sphare_pie_tsa*r2_sphare_tsa)

		else:
			print("please write the option not the value!!")		
	elif a.capitalize()=="Hemisphare":
	#2πr*r
		radius_hemisphare_TSA=float(input("enter the radius of hemisphare:>"))
		r2_hemisphare_tsa=radius_hemisphare_TSA*radius_hemisphare_TSA
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_hemisphare=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_hemisphare.capitalize()=="A":
			
			hemisphare_pie_tsa=22/7
			print("The CSA of hemiSphare is :>",2*hemisphare_pie_tsa*r2_hemisphare_tsa)

		elif pi_for_tsa_of_hemisphare.capitalize()=="B":
			hemisphare_pie_tsa=3.14
			print("The CSA of HemiSphare is :>",2*hemisphare_pie_tsa*r2_hemisphare_tsa)

		elif pi_for_tsa_of_hemisphare.capitalize()=="C":
			hemisphare_pie_tsa=3.141
			print("The CSA of HemiSphare is :>",2*hemisphare_pie_tsa*r2_hemisphare_tsa)

		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Frustum":
		slant_tsa_Frustum=float(input("enter slant hight of Frustum:>"))
		r1_frustum_tsa=float(input("enter frist radius of Frustum:>"))
		r2_frustum_tsa=float(input("enter second radius of Frustum:>"))
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_Frustum=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_Frustum.capitalize()=="A":
			#πl(r1+r2)
			r1_plus_r2_tsa=r1_frustum_tsa+r2_frustum_tsa
			Frustum_pie_tsa=22/7
			mitari=Frustum_pie_tsa*slant_tsa_Frustum
			print("the C.S.A of Frustum is:>",mitari*r1_plus_r2_tsa)
		elif pi_for_tsa_of_Frustum.capitalize()=="B":
			r1_plus_r2_tsa=r1_frustum_tsa+r2_frustum_tsa
			Frustum_pie_tsa=3.1
			mitari=Frustum_pie_tsa*slant_tsa_Frustum
			print("the C.S.A of Frustum is:>",mitari*r1_plus_r2_tsa+ar1+ar2)
		elif pi_for_tsa_of_Frustum.capitalize()=="C":
			r1_plus_r2_tsa=r1_frustum_tsa+r2_frustum_tsa
			Frustum_pie_tsa=3.14
			mitari=Frustum_pie_tsa*slant_tsa_Frustum
			print("the C.S.A of Frustum is:>",mitari*r1_plus_r2_tsa+ar1+ar2)
		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Hollow cylinder":	
		# 2π ( r1 + r2 )H
		r1hollowtsa=float(input("enter the inner radius of hollow cylinder:>"))
		r2hollowtsa=float(input("enter outer radius:>"))
		hofhollowtsa=float(input("enter hight of cylinder:>"))
		r1_plus_r2hollow_tsa=r1hollowtsa+r2hollowtsa
		
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pie_for_hollo_tsa=input("enter the option....for eg.a,b&c")
		if pie_for_hollo_tsa.capitalize()=="A":
			pie___=22/7
			print("the CSA of hollow cylinder is:>",2*pie___*r1_plus_r2hollow_tsa*hofhollowtsa)
		if pie_for_hollo_tsa.capitalize()=="B":
			pie___=3.14
			print("the CSA of hollow cylinder is:>",2*pie___*r1_plus_r2hollow_tsa*hofhollowtsa)
		if pie_for_hollo_tsa.capitalize()=="C":
			pie___=3.141
			print("the CSA of hollow cylinder is:>",2*pie___*r1_plus_r2hollow_tsa*hofhollowtsa)
		else:
			print("please write the option not the value!!")
	else:
		print("invalid input!")		

def vol():
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("wlecome to VOLUME finder:>")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("select a shape from given below and write code \n ------for example type cube for volume of cube------ \n  #>cube for 3dshape cube \n  #>cuboid for 3dshape cuboid \n  #>cone for 3dshape cone \n  #>cylinder for 3dshape cylinder")
	print("  #>sphare for 3dshape sphare \n  #>hemisphare for 3dshape hemisphare \n  #>frustum for 3dshape frustum of cone \n  #>hollow cylinder for 3dshape hollow cylinder \n")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("note-- please left a space between hollow and cylinder::")
	print("       please write the name of shape correctely!")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	a=input("enter the code:>")
	print("---------------------------------------------------")
	if a.capitalize()=="Cube":
		edge_t_s_a_=float(input("enter edge of cube:>"))
		rohit=edge_t_s_a_*edge_t_s_a_
		print("the VOLUME of Cube is:>",edge_t_s_a_*rohit)
	elif a.capitalize()=="Cuboid":
		len_T_S_A_=float(input("enter length of Cuboid:>"))
		bre_T_S_A_=float(input("enter brith of Cuboid:>"))
		hight_cuboid_tsa=float(input("enter hight of Cuboid:>"))
		lintobinvol=l*b
		print("the VOLUME of Cuboid is:>",h*lintobinvol)
	elif a.capitalize()=="Cylinder":
		radius_T_S_A_CYL=float(input("enter radius of Cylinder:>"))
		hight_tsa_Cyl=float(input("enter hight of Cylinder:>"))
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_cyl=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_cyl.capitalize()=="A":
			#πr^2h
			squareofrofcyl=radius_T_S_A_CYL*radius_T_S_A_CYL
			rsquareh=hight_tsa_Cyl*squareofrofcyl
			cyl_pie_tsa=22/7
			print("the VOLUME of Cylinder is:>",cyl_pie_tsa*rsquareh)
		elif pi_for_tsa_of_cyl.capitalize()=="B":
			squareofrofcyl=radius_T_S_A_CYL*radius_T_S_A_CYL
			rsquareh=hight_tsa_Cyl*squareofrofcyl
			cyl_pie_tsa=3.14
			print("the VOLUME of Cylinder is:>",cyl_pie_tsa*rsquareh)
		elif pi_for_tsa_of_cyl.capitalize()=="C":
			squareofrofcyl=radius_T_S_A_CYL*radius_T_S_A_CYL
			rsquareh=hight_tsa_Cyl*squareofrofcyl
			cyl_pie_tsa=3.141
			print("the VOLUME of Cylinder is:>",cyl_pie_tsa*rsquareh)	
		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Cone":
		#1/3πr^2H
		radius_T_S_A_Cone=float(input("enter the radius of Cone:>"))
		slant_tsa_Cone=float(input("enter the hight of Cone:>"))
		square_of_r_is_equal=radius_T_S_A_Cone*radius_T_S_A_Cone
		huponthreeis=slant_tsa_Cone/3
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_cone=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_cone.capitalize()=="A":
			cone_pie_tsa=22/7
			print("the VOLUME of Cone is:>",cone_pie_tsa*square_of_r_is_equal*huponthreeis)
		elif pi_for_tsa_of_cone.capitalize()=="B":
			cone_pie_tsa=3.14
			print("the VOLUME of Cone is:>",cone_pie_tsa*square_of_r_is_equal*huponthreeis)
		elif pi_for_tsa_of_cone.capitalize()=="C":
			cone_pie_tsa=3.141
			print("the VOLUME of Cone is:>",cone_pie_tsa*square_of_r_is_equal*huponthreeis)	
		else:
			print("please write the option not the value!!")
	elif a.capitalize()=="Sphare":
		#4/3π(r*r*r)
		radius_sphare_TSA=float(input("enter the radius of sphare:>"))
		r2_sphare_tsa=radius_sphare_TSA*radius_sphare_TSA
		r3_sphare_vol=r2_sphare_tsa*radius_sphare_TSA
		val_vol_sphare=4/3
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_sphare=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_sphare.capitalize()=="A":
			
			sphare_pie_tsa=22/7
			print("The VOLUME of Sphare is :>",val_vol_sphare*sphare_pie_tsa*r3_sphare_vol)

		elif pi_for_tsa_of_sphare.capitalize()=="B":
			sphare_pie_tsa=3.14
			print("The VOLUME of Sphare is :>",val_vol_sphare*sphare_pie_tsa*r3_sphare_vol)

		elif pi_for_tsa_of_sphare.capitalize()=="C":
			sphare_pie_tsa=3.141
			print("The VOLUME of Sphare is :>",val_vol_sphare*sphare_pie_tsa*r3_sphare_vol)

		else:
			print("please write the option not the value!")			
	elif a.capitalize()=="Hemisphare":
		#2/3π(r*r*r) 
		radius_sphare_TSA=float(input("enter the radius of Hemisphare:>"))
		r2_sphare_tsa=radius_sphare_TSA*radius_sphare_TSA
		r3_sphare_vol=r2_sphare_tsa*radius_sphare_TSA
		val_vol_sphare=2/3
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value! ")
		pi_for_tsa_of_sphare=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_sphare.capitalize()=="A":
			
			sphare_pie_tsa=22/7
			print("The VOLUME of Sphare is :>",val_vol_sphare*sphare_pie_tsa*r3_sphare_vol)

		elif pi_for_tsa_of_sphare.capitalize()=="B":
			sphare_pie_tsa=3.14
			print("The VOLUME of Sphare is :>",val_vol_sphare*sphare_pie_tsa*r3_sphare_vol)

		elif pi_for_tsa_of_sphare.capitalize()=="C":
			sphare_pie_tsa=3.141
			print("The VOLUME of Sphare is :>",val_vol_sphare*sphare_pie_tsa*r3_sphare_vol)

		else:
			print("please write the option not the value!")			
	elif a.capitalize()=="Frustum":
		slant_tsa_Frustum=float(input("enter hight of Frustum:>"))
		r1_frustum_tsa=float(input("enter frist radius of Frustum:>"))
		r2_frustum_tsa=float(input("enter second radius of Frustum:>"))
		val_vol_frus=1/3
		r1squareoffrus=r1_frustum_tsa*r1_frustum_tsa
		r2squareoffrus=r2_frustum_tsa*r2_frustum_tsa
		r12plusr22is=r1squareoffrus+r2squareoffrus
		r1intor2frus=r1_frustum_tsa*r2_frustum_tsa
		braket=r12plusr22is+r1intor2frus
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pi_for_tsa_of_Frustum=input("enter the option among these with option name a,b&c:>")
		if pi_for_tsa_of_Frustum.capitalize()=="A":
			# (1/3) * π * h * (r1^2 + r2^2 + (r1 * r2)).
			Frustum_pie_tsa=22/7
			print("the VOLUME of Frustum is:>",val_vol_frus*Frustum_pie_tsa*slant_tsa_Frustum*braket)
		elif pi_for_tsa_of_Frustum.capitalize()=="B":
			Frustum_pie_tsa=3.1
			mitari=Frustum_pie_tsa*slant_tsa_Frustum
			print("the VOLUME of Frustum is:>",val_vol_frus*Frustum_pie_tsa*slant_tsa_Frustum*braket)
		elif pi_for_tsa_of_Frustum.capitalize()=="C":
			Frustum_pie_tsa=3.14
			print("the VOLUME of Frustum is:>",val_vol_frus*Frustum_pie_tsa*slant_tsa_Frustum*braket)
		else:
			print("please write the option not the value!")
	elif a.capitalize()=="Hollow cylinder":
		#πh(r1^2-r2^2)
		h=float(input("enter hight of Hollow cylinder:>"))
		r1=float(input("enter outer radius:>"))
		r2=float(input("enter inner radius:>"))
		r1_square_hollow=r1*r1
		r2_square_hollow=r2*r2
		r1_square_minus_r2_square=r1_square_hollow-r2_square_hollow
		print(" a> π=22/7 \n b>π=3.14 \n c>π=3.141 \n \n please write the option not the value!")
		pie_for_hollo_tsa=input("enter the option....for eg.a,b&c")
		if pie_for_hollo_tsa.capitalize()=="A":
			pie___=22/7
			print("the CSA of hollow cylinder is:>",pie___*h*r1_square_minus_r2_square)
		if pie_for_hollo_tsa.capitalize()=="B":
			pie___=3.14
			print("the CSA of hollow cylinder is:>",pie___*h*r1_square_minus_r2_square)
		if pie_for_hollo_tsa.capitalize()=="C":
			pie___=3.141
			print("the CSA of hollow cylinder is:>",pie___*h*r1_square_minus_r2_square)
		else:
			print("invalid input!")
	else:
		print("please write the option not the value!")

def cond():
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("-----welcome to surfacearea and volume portal------")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("in this portal you can find C.S.A, T.S.A & VOLUME of any 3d shape!")
	print("---------------------------------------------------")
	print("---------------------------------------------------")
	print("1> to find T.S.A type/write TSA \n2>to find C.S.A type/write CSA \n3>to find VOLUME type/write VOL")
	condition=input("enter your choice:>")
	if condition.upper()=="TSA":
		T_S_A()
	elif condition.upper()=="CSA":
		C_S_A()
	elif condition.upper()=="VOL":
		vol()
	else:
		print("invalid input!")
		cond()

cond()
choice=input(">>>>>to continue press y other wise press any key:>")
while choice.upper()=="Y":
	cond()
	choice=input("do you want to continue press y other wise press any key:>")
	if choice.upper()=="Y":
		continue
	else:
		break	
		exit()