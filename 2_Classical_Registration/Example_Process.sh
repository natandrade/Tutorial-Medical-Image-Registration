#bash Example_Process.sh 

#Example with FLIRT - FSL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki

#VERSION 0.0.0

#First Step: Learn Bash
#Second Step: Install FSL
#Third Step: Bash executable

#Name your computer
name_computer="/home/name_computer/"

echo "Put folders in call bash "Target" "Source""

#Read folders 
T1=`ls ${1}/*.nii.gz`
t2=`ls ${2}/*.nii.gz`

i=1
#CREAT VECTOR
for t2s in $t2; do
		T2[i]=${t2s}
		i=$(($i+1));
done

#a ->  -cost: mutualinfo,corratio,normcorr,normmi,leastsq,labeldiff
a[1]='mutualinfo'
a[2]='corratio'
a[3]='normcorr'
a[4]='normmi'
a[5]='leastsq'
a[6]='labeldiff'

#b -> -searchcost: {mutualinfo,corratio,normcorr,normmi,leastsq,labeldiff,bbr}  (default is corratio)

#c -> -interp: {trilinear,nearestneighbour,sinc,spline}  (final interpolation: def - trilinear)
c[1]='trilinear'
c[2]='nearestneighbour'
c[3]='sinc'
c[4]='spline'

#d -dof:  <number of transform dofs>   (default is 12)


#Test
for a1 in {1..1}; do   
  for c1 in {4..4}; do   
   for d1 in {12..12}; do   
   
      #RESULT MOVING IMAGE
      Resultados_fim="/home/name_computer/Result_Flirt_${a1}_${c1}_${d1}"
      echo "$Resultados_fim"
      mkdir -p "$Resultados_fim"

      #MATRIX OUT
      MAT_FIM="/home/name_computer/Result_Flirt_MAT_${a1}_${c1}_${d1}"
      echo "$MAT_FIM"
      mkdir -p "$MAT_FIM"
      
      #CREATE TIME STUDY
      tempo="/home/name_computer/Result_Flirt_Tempo_${a1}_${c1}_${d1}"
      echo "$tempo"
      mkdir -p "$tempo"

      i=1
      for t1 in $T1; do
          echo "$i"
          echo "Prever a Transformação"
          echo "fsl5.0-flirt -in "/home/$name_computer/${T2[i]}" -ref "/home/$name_computer/${t1}" -out ${Resultados_fim}/"T2_T1_${i}" -omat ${MAT_FIM}/"t1e_ida_t2m_${i}.mat" -dof $d1 -cost ${a[a1]} -searchcost ${a[a1]} -interp ${c[c1]}" 
          echo -e "\n"
          /usr/bin/time -o $tempo/${i}_time.txt -f "\n%E elapsed,\n%U user,\n%S system,\n%M memory\n%x status" fsl5.0-flirt -in "/home/$name_computer/${T2[i]}" -ref "/home/$name_computer/${t1}" -out ${Resultados_fim}/"T2_T1_${i}" -omat ${MAT_FIM}/"t1e_ida_t2m_${i}.mat" -dof $d1 -cost ${a[a1]} -searchcost ${a[a1]} -interp ${c[c1]} 
          i=$(($i+1)); 
      done
   done
  done
done
