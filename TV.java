package ex0701;

public class TV {

	 int channel;
	 
	 public TV() {}
	 
	 public TV(int intValue) {
		 this.channel=intValue;
		 
	 }
	 protected void channelUP() {
		 channel = channel +1;
	 }
	 
	 private void channelDown() {
		 channel= channel -1;
		 if(channel < 0) {
			 channel = 0;
		 }
	 }
	 
	 public static void main(String args[]) {
		TV objTV = new TV(11);	
		System.out.println("현재 채널은"+objTV.channel + "번호입니다.");
		
		objTV.channelDown();
		
		System.out.println("채널을 바꿈");
		
		System.out.println("현재 채널은"+objTV.channel);
		
	 }
}
