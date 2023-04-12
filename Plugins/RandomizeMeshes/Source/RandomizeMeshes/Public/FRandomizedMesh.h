#pragma once

#include "CoreMinimal.h"
#include "FRandomizedMesh.generated.h"

USTRUCT(BlueprintType)
struct FRandomizedMesh
{
	GENERATED_BODY()
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
	FString Name;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
		FVector Position;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
		FRotator Rotation;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
		FVector Scale;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
		FString Type;

};
