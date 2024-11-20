class Solution {
    public int[] twoSum(int[] nums, int target) {
        return twoSumWithHashMap(nums, target);
    }

    public int[] twoSumWithHashMap(int[] nums, int target) {
        Map<Integer, Integer> indices = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            indices.put(nums[i], i);
        }

        for (int j = 0; j < nums.length; j++ ) {
            Integer matching = indices.get(target - nums[j]);

            if (matching != null && matching != j) {
                if (matching < j) return new int[] {matching, j};
                else return new int[] {j, matching};
            } 
        }

        return new int[0];
    }

    public int[] twoSumWithBruteForce(int[] nums, int target) {
        int first = 0;
        int second = 1;

        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j< nums.length; j++) {
                if (nums[i] + nums[j] == target) return new int[]{i, j};
            }
        }

        return new int[2];
    }
}
