package ex0701;

public class BrandTV extends TV {

	String brand;
	
	public BrandTV(int intValue, String strValue) {
		super.channel = intValue;
		this.brand = strValue;
	}
	
	public static void main(String[] args) {
		BrandTV objTV = new BrandTV(11, "�ＺTV");
		objTV.channelUP();
		System.out.println(objTV.brand+" ���� ä���� "+ objTV.channel + "���Դϴ�");
	}
}
