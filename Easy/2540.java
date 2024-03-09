class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        int l1=nums1.length,l2=nums2.length;
        int t1=0,t2=0;
        while (t1<l1 && t2<l2){
            if(nums1[t1]==nums2[t2]) return nums1[t1];
            if(nums1[t1]>nums2[t2]) t2++;
            else t1++;
        } 
    return -1;
    }
}